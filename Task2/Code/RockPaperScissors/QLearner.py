import math
import numpy as np


class QLearner:

    def __init__(self,
                 decay=0.9,
                 learning_rate=0.00005,
                 strategy_layout=[33, 33, 34],
                 normalization_constant=1,
                 temperature=1):
        self.q_values = {}
        self.learning_rate = learning_rate
        self.decay = decay
        self.strategy_layout = strategy_layout
        self.actions = range(len(strategy_layout))

        self.normalization_constant = normalization_constant
        self.temperature = temperature
        for j in range(len(self.strategy_layout)):
            self.q_values[j] = math.log(self.normalization_constant * self.strategy_layout[j]/100) * self.temperature

    def learn(self, current_state, new_state, reward, agent_action, opp_action):
        old_q_value = self.q_values.get(agent_action)
        q_max = max([self.q_values.get(_action) for _action in self.actions])
        new_q_value = old_q_value + self.learning_rate * (reward + self.decay * q_max - old_q_value)

        # Update the Q value
        self.q_values[agent_action] = new_q_value
        # Update normalization constant
        self.normalization_constant = 0
        for i in range(len(self.strategy_layout)):
            self.normalization_constant += math.exp(self.q_values.get(i) / self.temperature)

    def choose_action(self, state):
        probability_distribution = []
        for a in self.actions:
            p_a = (1/self.normalization_constant) * math.exp(self.q_values.get(a) / self.temperature)
            probability_distribution.append(p_a)
        probability = np.random.choice(probability_distribution, p=probability_distribution)
        action = np.argmax(probability_distribution == probability)
        # print(action, "playerA")
        return action, probability_distribution

    def reset(self):
        for j in range(len(self.strategy_layout)):
            self.q_values[j] = math.log(self.normalization_constant * self.strategy_layout[j]/100) * self.temperature

    def __str__(self):
        return "QLearner"
