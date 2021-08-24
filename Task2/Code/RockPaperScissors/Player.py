ACTIONS = ['R', 'P', 'S']


class Player:

    def __init__(self, name, learner):
        self.name = name
        self.reward = []
        self.last_action = None
        self.learner = learner

    def choose_action(self, state):
        act, probability_distribution = self.learner.choose_action(state=state)
        action = ACTIONS[act]
        return action, probability_distribution

    def learn(self, state, new_state, agent_action, opp_action, reward=0):
        agent_action = ACTIONS.index(agent_action)
        opp_action = ACTIONS.index(opp_action)
        self.reward.append(reward)
        if self.last_action:
            self.learner.learn(current_state=state, agent_action=agent_action, opp_action=opp_action, reward=reward,
                               new_state=new_state)
        self.last_action = True

    def reset(self):
        self.reward = []
        self.last_action = None
        self.learner.reset()

    def __str__(self):
        name = str(self.learner) + self.name
        return str(name)
