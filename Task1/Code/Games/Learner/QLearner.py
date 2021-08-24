import random


class QLearner:

    def __init__(self,
                 name,
                 decay=0.9,
                 learning_rate=0.00005,
                 observation_size=4,
                 epsilon=0.12,
                 percentage=50):
        self.name = name
        self.observation_size = observation_size
        self.values = {}
        # step size, for now, we always learn a bit on everything.
        self.learning_rate = learning_rate
        # discount factor
        self.decay = decay
        self.actions = range(2)
        # Greedy algo to explore
        self.epsilon = epsilon
        self.value_initialization = 1
        self.percentage = percentage

    def learn(self, state, action, reward, new_state):
        # We take only the last episode
        state = tuple(state[-self.observation_size:])  # We take only the last episode
        new_state = tuple(new_state[-self.observation_size:])

        old_value = self.values.get((state, action), self.value_initialization)  # try to get, otherwise init at 0.5

        qmax = max([self.values.get((new_state, _action), self.value_initialization) for _action in self.actions])
        # print(f'{self.name} avec {qmax}')
        new_value = old_value + self.learning_rate * (reward + self.decay*qmax - old_value)
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
                ret = 0
            else:
                ret = 1

        return ret

    def reset(self):
        self.values = {}
        self.N = 0

    def set_initial_strategy(self, strat):
        self.initial_strategy = strat

    def __str__(self):
        return "QLearner"
