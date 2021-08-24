import random

# Greedy exploration Q-Learner


class QLearner:

    def __init__(self,
                 decay=0.9,
                 learning_rate=0.00005,
                 observation_size=1,
                 epsilon=0.12,
                 q_value_init=1,
                 strategy_layout=[33, 33, 34]):
        self.observation_size = observation_size
        self.q_values = {}
        self.learning_rate = learning_rate
        self.decay = decay
        self.epsilon = epsilon
        self.q_value_init = q_value_init
        self.strategy_layout = strategy_layout
        self.actions = range(len(strategy_layout))
        self.strategy_probabilities = []
        for (i, strategy_i) in enumerate(strategy_layout):
            self.strategy_probabilities += [i] * strategy_i
        self.sum_probabilities = len(self.strategy_probabilities)

    def learn(self, current_state, new_state, reward, self_action, opp_action):
        # We are only interested in the last episodes
        current_state = tuple(current_state[-self.observation_size:])
        new_state = tuple(new_state[-self.observation_size:])
        # Try to retrieve the old q_value for a given (s,a), if it does not exist initialize it at q_value_init
        old_q_value = self.q_values.get((current_state, self_action), self.q_value_init)
        q_max = max([self.q_values.get((new_state, _action), self.q_value_init) for _action in self.actions])
        new_q_value = old_q_value + self.learning_rate * (reward + self.decay * q_max - old_q_value)
        self.q_values[current_state, self_action] = new_q_value

    def choose_action(self, state):
        # If no state exists yet, or if epsilon-exploration conditions are verified, an action is randomly chosen
        if not state or random.random() < self.epsilon:
            return self.strategy_probabilities[random.randint(0, self.sum_probabilities-1)]
        # We are only interested in the last episodes
        state = tuple(state[-self.observation_size:])
        # Verify whether for the current state two actions have the same q-value. If so, an action is randomly chosen
        # TODO verify this what if third action is not the same?
        for a1 in self.actions:
            for a2 in self.actions:
                if not a1 == a2 and self.q_values.get((state, a1), self.q_value_init) == self.q_values.get((state, a2), self.q_value_init):
                    return self.strategy_probabilities[random.randint(0, self.sum_probabilities-1)]
        # Return the best action for the current state
        return max(self.actions, key=lambda action: self.q_values.get((state, action), self.q_value_init))

    def reset(self):
        self.q_values = {}

    def __str__(self):
        return "QLearner"
