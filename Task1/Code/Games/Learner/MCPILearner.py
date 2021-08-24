"""
Monte Carlo Policy Iteration learner. Comes from "Machine Learning and Inductive Inference" of H. Blockeel, pg259
"""


import random


class MCIPLearner:

    def __init__(self,
                 name,
                 decay=0.9,
                 observation_size=2,
                 epsilon=0.1,
                 percentage=50):
        self.name = name
        self.observation_size = observation_size
        self.values = {}
        # discount factor
        self.decay = decay
        self.actions = range(2)
        # Greedy algo to explore
        self.epsilon = epsilon
        self.percentage = percentage
        self.value_initialization = 0.5

    def learn(self, state, action, reward, new_state):
        # We take only the last episode
        state = tuple(state[-self.observation_size:])  # We take only the last episode

        old_value = self.values.get((state, action), self.value_initialization)  # try to get, otherwise init at 0.5

        # print(f'{self.name} avec {qmax}')
        new_value = reward + self.decay * old_value
        self.values[state, action] = new_value
        # print(f'{self.name} avec {self.values}')

    def choose(self, state):
        if not state:  # if we don't have any state, randomly do an action.
            i = random.randint(1, 100)
            if i < self.percentage:
                return 0
            else:
                return 1

        state = tuple(state[-self.observation_size:])  # We take only the last episode

        if random.random() < self.epsilon:  # We explore
            i = random.randint(1, 100)
            if i < self.percentage:
                return 0
            else:
                return 1

        ret = max(self.actions, key=lambda action: self.values.get((state, action), self.value_initialization))

        dic = {}
        for action in self.actions:
            val = self.values.get((state, action), self.value_initialization)
            dic[action] = val

        if dic[0] == dic[1]:
            i = random.randint(1, 100)
            if i < self.percentage:
                return 0
            else:
                return 1

        return ret

    def reset(self):
        self.values = {}

    def __str__(self):
        return "MCILearner"
