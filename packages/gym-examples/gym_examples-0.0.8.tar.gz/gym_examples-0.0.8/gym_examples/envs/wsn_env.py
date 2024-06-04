import gym
import numpy as np
from gym.spaces import Discrete, Box, Tuple

class WSNRoutingEnv(gym.Env):
    def __init__(self, n_sensors=10, coverage_radius=0.5, max_hops=5):
        self.n_sensors = n_sensors
        self.n_agents = n_sensors
        self.coverage_radius = coverage_radius
        self.max_hops = max_hops

        self.observation_space = Tuple(tuple([Box(np.array([[0], [0]]), np.array([[1], [1]]), dtype=np.float32)] * self.n_agents))
        self.action_space = Tuple(tuple([Discrete(self.n_sensors + 1)] * self.n_agents))
        
        self.reset()

    def reset(self):
        self.sensor_positions = np.random.rand(self.n_sensors, 2) * self.coverage_radius
        self.distance_to_base = np.linalg.norm(self.sensor_positions - np.array([0.5, 0.5]), axis=1)
        self.remaining_energy = np.ones(self.n_sensors)
        self.current_sensor = np.random.randint(self.n_sensors)
        self.step_count = 0
        
        return self._get_observation()

    def step(self, actions):
        rewards = [0] * self.n_sensors
        dones = [False] * self.n_sensors

        for i, action in enumerate(actions):
            if action not in range(self.n_sensors + 1):
                raise ValueError("Invalid action!")

            self.remaining_energy[i] -= 0.1

            if action == self.n_sensors:
                rewards[i] = 1.0
                dones[i] = True
            else:
                self.current_sensor = action
                self.distance_to_base[i] = np.linalg.norm(self.sensor_positions[i] - np.array([0.5, 0.5]))

                reward = (self.distance_to_base[i] - np.max(self.distance_to_base)) / self.coverage_radius - 0.1
                done = (self.distance_to_base[i] <= self.coverage_radius) or (self.remaining_energy[i] <= 0) or (self.step_count >= self.max_hops)
                rewards[i] = reward
                dones[i] = done
                self.step_count += 1

                if done and self.distance_to_base[i] > self.coverage_radius:
                    rewards[i] -= 0.5

        return self._get_observation(), rewards, dones, {}

    def _get_observation(self):
        return [(e, d) for e, d in zip(self.remaining_energy, self.distance_to_base)]