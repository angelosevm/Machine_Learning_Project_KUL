class NonLearner:

    def __init__(self,
                 name,
                 choice=0):
        self.name = name
        self.choice = choice

    def learn(self, state, action, reward, new_state):
        pass

    def choose(self, state):
        return self.choice

    def reset(self):
        pass

    def __str__(self):
        return "NonLearner"+str(self.choice)
