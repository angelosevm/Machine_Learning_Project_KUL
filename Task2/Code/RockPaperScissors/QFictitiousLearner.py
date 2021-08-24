import math
import numpy as np


# Q Fictitious Learner with Boltzmann exploration


class QFictitiousLearner:

    def __init__(self,
                 decay=0.9,
                 learning_rate=0.00005,
                 strategy_layout=[90, 5, 5],
                 normalization_constant=400,
                 temperature=1):
        self.q_values = {}
        self.learning_rate = learning_rate
        self.decay = decay
        self.strategy_layout = strategy_layout
        self.actions = [tuple((i, j)) for i in range(len(strategy_layout)) for j in range(len(strategy_layout))]
        self.normalization_constant = normalization_constant
        self.temperature = temperature
        self.opponent_counts = [0, 0, 0]
        self.opponent_probabilities = [0.0, 0.0, 0.0]
        self.total_count = 0
        # Initialize the expectancy matrix
        self.E = [0.0] * len(strategy_layout)
        for i in range(len(self.strategy_layout)):
            self.E[i] = math.log(self.normalization_constant * self.strategy_layout[i]/100) * self.temperature
            for j in range(len(self.strategy_layout)):
                self.q_values[(i, j)] = self.E[i]

    def learn(self, current_state, new_state, reward, agent_action, opp_action):
        joint_action = tuple((agent_action, opp_action))
        old_q_value = self.q_values.get(joint_action)
        q_max = max([self.q_values.get(_action) for _action in self.actions])
        new_q_value = old_q_value + self.learning_rate * (reward + self.decay * q_max - old_q_value)
        # Update the Q value
        self.q_values[joint_action] = new_q_value
        # Update the count of the given opponent's play
        self.opponent_counts[opp_action] += 1
        self.total_count += 1
        # Update the probabilities of the opponent's play
        for i in range(len(self.strategy_layout)):
            self.opponent_probabilities[i] = self.opponent_counts[i] / self.total_count
        # Update expectancy matrix
        for i in range(len(self.E)):
            self.E[i] = self.q_values.get((i, 0)) * self.opponent_probabilities[0] + \
                   self.q_values.get((i, 1)) * self.opponent_probabilities[1] + \
                   self.q_values.get((i, 2)) * self.opponent_probabilities[2]

        # Update normalization constant
        self.normalization_constant = 0
        for i in range(len(self.strategy_layout)):
            self.normalization_constant += math.exp(self.E[i] / self.temperature)

    def choose_action(self, state):
        probability_distribution = []
        for i in range(len(self.strategy_layout)):
            p_a = (1 / self.normalization_constant) * math.exp(self.E[i] / self.temperature)
            probability_distribution.append(p_a)
        probability = np.random.choice(probability_distribution, p=probability_distribution)
        action = np.argmax(probability_distribution == probability)
        return action, probability_distribution

    def reset(self):
        self.q_values.clear()
        self.opponent_counts = [0, 0, 0]
        self.opponent_probabilities = [0, 0, 0]
        self.total_count = 0

    @staticmethod
    def beat(action):
        return action - 1 if action > 0 else 2

    def __str__(self):
        return "QFictitiousLearner"
