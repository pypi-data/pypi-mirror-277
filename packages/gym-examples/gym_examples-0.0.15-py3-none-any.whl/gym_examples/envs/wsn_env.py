import gym
import numpy as np
from gym.spaces import Discrete, Box, Tuple
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import torch
import torch.nn as nn
import torch.nn.functional as F

# Define the network parameters for the final reward function
input_dim = 3  # number of individual rewards
output_dim = 1  # final reward


stats_file_path_base = 'C:\\Users\\djime\\Documents\\PHD\\THESIS\\CODES\\RL_Routing\\Results_EPyMARL\\stats_over_time.csv'
Eelec = 50e-9  # energy consumption per bit in joules
Eamp = 100e-12  # energy consumption per bit per square meter in joules
info_amount = 3072  # data size in bits

# Define the final reward function using an attention mechanism
class Attention(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(Attention, self).__init__()  # Call the initializer of the parent class (nn.Module)
        self.input_dim = input_dim  # Set the input dimension of the network
        self.output_dim = output_dim  # Set the output dimension of the network
        self.linear1 = nn.Linear(input_dim, 64)  # Define the first linear layer. It takes input of size 'input_dim' and outputs size '64'
        self.linear2 = nn.Linear(64, output_dim)  # Define the second linear layer. It takes input of size '64' and outputs size 'output_dim'

    def forward(self, x):
        x = F.relu(self.linear1(x))  # Pass the input through a linear layer and a ReLU activation function
        attention_weights = F.softmax(x, dim=0)  # Apply the softmax function to get the attention weights
        x = attention_weights * x  # Multiply the input by the attention weights
        x = self.linear2(x)  # Pass the result through another linear layer
        return x

# Calculate the reward
net = Attention(input_dim, output_dim)
net = net.double()  # Convert the weights to Double


class WSNRoutingEnv(gym.Env):
    def __init__(self, n_sensors=10, coverage_radius=0.25, max_hops=30):

        time_id = str(datetime.timestamp(datetime.now()))
        self.stats_file_path = stats_file_path_base + '_' + time_id # Set the file path

        # Initialize the CSV file with headers
        with open(self.stats_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['step_count', 'Average remaining energy',  
                             'Total energy consumption of WSN', 'The number of sensors without energy'])

        self.n_sensors = n_sensors
        self.n_agents = n_sensors
        self.coverage_radius = coverage_radius
        self.max_hops = max_hops

        self.observation_space = Tuple(tuple([Box(np.array([[0], [0]]), np.array([[1], [1]]), dtype=np.float32)] * self.n_agents))
        self.action_space = Tuple(tuple([Discrete(self.n_sensors + 1)] * self.n_agents))
        
        self.reset()

    def reset(self):
        self.sensor_positions = np.random.rand(self.n_sensors, 2)
        self.distance_to_base = np.linalg.norm(self.sensor_positions - np.array([0.5, 0.5]), axis=1)
        # Initialize remaining energy of each sensor to 1 joule
        self.remaining_energy = np.ones(self.n_sensors)
        self.current_sensor = np.random.randint(self.n_sensors)
        self.consumption_energy = np.zeros(self.n_sensors)
        self.step_count = 0
    
        
        return self._get_observation()

    def step(self, actions):
        rewards = [0] * self.n_sensors
        dones = [False] * self.n_sensors

        for i, action in enumerate(actions):
            if action not in range(self.n_sensors + 1):
                raise ValueError("Invalid action!")
            
            # If a sensor tries to transmit data to itself, ignore this action
            if action == i:
                continue

            self.distance_to_base[i] = np.linalg.norm(self.sensor_positions[i] - np.array([0.5, 0.5]))
            if action == self.n_sensors:
                rewards[i] = 1.0
                dones[i] = True
                # Calculate the energy consumption for transmitting data to the next hop
                distance_to_next_hop = self.distance_to_base[i]
                self.consumption_energy[i] += info_amount * (Eelec + Eamp * distance_to_next_hop**2) # energy consumption for transmitting data
                self.remaining_energy[i] -= self.consumption_energy[i]
            else:
                # Calculate the energy consumption for transmitting data to the next hop
                distance_to_next_hop = np.linalg.norm(self.sensor_positions[i] - self.sensor_positions[action])
                self.consumption_energy[i] += info_amount * (Eelec + Eamp * distance_to_next_hop**2) # energy consumption for transmitting data
                self.consumption_energy[action] += info_amount * Eelec # energy consumption for receiving data
                self.remaining_energy[i] -= self.consumption_energy[i]
                self.remaining_energy[action] -= self.consumption_energy[action]

                self.current_sensor = action
                
                self.distance_to_base[action] = np.linalg.norm(self.sensor_positions[action] - np.array([0.5, 0.5]))

                # Calculate the angle between the current sensor, the next hop, and the base station
                vector_to_next_hop = self.sensor_positions[action] - self.sensor_positions[i]
                vector_to_base = np.array([0.5, 0.5]) - self.sensor_positions[i]
                cosine_angle = np.dot(vector_to_next_hop, vector_to_base) / (np.linalg.norm(vector_to_next_hop) * np.linalg.norm(vector_to_base))
                angle = np.arccos(np.clip(cosine_angle, -1, 1))  # in radians

                distances_to_sensors = np.linalg.norm(self.sensor_positions - self.sensor_positions[i], axis=1)
                is_within_coverage = distances_to_sensors <= self.coverage_radius
                # Calculate the average remaining energy of all sensors within the coverage radius                
                sensors_within_coverage = self.remaining_energy[is_within_coverage]
                average_remaining_energy = sensors_within_coverage.mean()

                # Calculate the sum of total consumption energy of all sensors within the coverage radius
                sensors_within_coverage = self.consumption_energy[is_within_coverage]
                average_consumption_energy = sensors_within_coverage.mean()

                # Calculate individual rewards
                reward_angle = 1 - (np.abs(angle) / np.pi)
                reward_distance = 1 - (distance_to_next_hop / self.coverage_radius)
                reward_energy = average_remaining_energy - average_consumption_energy
                rewards_individual = torch.tensor([reward_angle, reward_distance, reward_energy], dtype=torch.double)

                # Calculate final reward
                final_reward = net(rewards_individual)
                done = (self.remaining_energy[i] <= 0) or (self.step_count >= self.max_hops)
                rewards[i] = final_reward
                dones[i] = done
                self.step_count += 1

                if done and self.distance_to_base[action] > self.coverage_radius:
                    rewards[i] -= 0.5

        # Add a small random displacement to each sensor's position
        displacement = np.random.normal(scale=0.01, size=2)
        self.sensor_positions[i] += displacement

        # Make sure the new position is within the range [0, 1]
        if (np.any(self.sensor_positions[i] < 0)) or (np.any(self.sensor_positions[i] > 1)):
            self.sensor_positions[i] -= displacement

        # Append the stats to the CSV file
        with open(self.stats_file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.step_count, self.remaining_energy.mean(), self.consumption_energy.sum(), 
                             (self.remaining_energy <= 0).sum()])

        return self._get_observation(), rewards, dones, {}

    def _get_observation(self):
        return [(e, d) for e, d in zip(self.remaining_energy, self.distance_to_base)]