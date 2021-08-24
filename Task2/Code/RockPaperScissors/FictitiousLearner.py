import random

# Implementation of the fictitious learner

PAYOFF = [[0, -1, 1],
          [1, 0, -1],
          [-1, 1, 0]]


class FictitiousLearner:

    def __init__(self,
                 strategy_layout=[33, 33, 34]):
        self.strategy_probabilities = []
        for (i, strategy_i) in enumerate(strategy_layout):
            self.strategy_probabilities += [i] * strategy_i
        # Rock = 0, paper = 1, scissors = 2
        self.opponent_counts = strategy_layout
        self.total_count = sum(self.opponent_counts)
        self.opponent_probabilities = [x/self.total_count for x in self.opponent_counts]

    def learn(self, current_state, new_state, reward, agent_action, opp_action):
        # Update the count of the given opponent's play
        self.opponent_counts[opp_action] += 1
        self.total_count += 1
        # Update the probabilities of the opponent's play
        for i in range(len(self.opponent_probabilities)):
            self.opponent_probabilities[i] = self.opponent_counts[i] / self.total_count

    def choose_action(self, state):
        # Expectancy matrix
        E = [0.0] * 3
        for i in range(3):
            E[i] = PAYOFF[i][0] * self.opponent_probabilities[0] + \
                   PAYOFF[i][1] * self.opponent_probabilities[1] + \
                   PAYOFF[i][2] * self.opponent_probabilities[2]
        max_expectancy_value = max(E)
        current_action = list()
        for i in range(3):
            if E[i] == max_expectancy_value:
                current_action.append(i)

        # Extract the probabilities from the utilities
        Eprime = [(x + 1) for x in E]
        probabilities = [x/sum(Eprime) for x in Eprime]
        return random.choice(current_action), probabilities

    def reset(self):
        self.total_count = 0
        self.opponent_counts = {0: 0, 1: 0, 2: 0}
        self.opponent_probabilities = [0, 0, 0]

    @staticmethod
    def beat(action):
        return action - 1 if action > 0 else 2

    def __str__(self):
        return "FictitiousLearner"
