ACTIONS = ['H', 'T']

class Gambler:

    def __init__(self, name, learner):
        self.name = name
        self.reward = []
        self.last_action = None
        self.actions = []
        self.learner = learner

    def strategy(self, state):
        action = ACTIONS[self.learner.choose(state=state)]
        self.actions.append(action)
        return action

    def punish(self, state, action, reward, new_state):
        action = ACTIONS.index(action)
        self.reward.append(reward)
        if self.last_action:
            self.learner.learn(state=state, agent_action=action, reward=reward, new_state=new_state)
        self.last_action = True

    def reset(self):
        self.reward = []
        self.last_action = None
        self.actions = []
        self.learner.reset()

    def __str__(self):
        name = str(self.learner) + self.name
        return str(name)
