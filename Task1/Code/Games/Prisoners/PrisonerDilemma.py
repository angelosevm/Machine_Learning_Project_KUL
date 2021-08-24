"""
Python implementation of the Prisoners.py's dilemma.
Pareto optimal: no individual can be made better off without someone else being worse off.
Hicks optimal: the sum of the payoffs of all players is the maximum it could possibly be.
Nash equilibrium: no individual has an incentive to unilaterally change their strategy.
0 = Deny
1 = Confess
"""

learning_rate = 0.5


class PrisonerDilemma:

    def __init__(self, prisoner1, prisoner2):
        self.prisoner1 = prisoner1
        self.prisoner2 = prisoner2
        self.data = {1: [], 2: []}

        self.REWARD = 3  # put 4 here?
        self.SUCKER = 0
        self.TEMPTATION = 5
        self.PUNISHMENT = 1

    def play(self, moves=1):
        """Play a number moves time"""
        for _ in range(0, moves):
            self.play_a_move()

    def play_a_move(self):
        """
        Execute one iteration of the game
        We ask for strategy and then save the results
        """
        # The state here is the history of the player results
        action_a = self.prisoner1.strategy(state=self.data[1])
        action_b = self.prisoner2.strategy(state=self.data[2])

        # Game mechanic
        if action_a == action_b == "D":
            return_a, return_b = self.PUNISHMENT, self.PUNISHMENT
        elif action_a == "D" and action_b == "C":
            return_a = self.TEMPTATION
            return_b = self.SUCKER
        elif action_a == "C" and action_b == "D":
            return_a = self.SUCKER
            return_b = self.TEMPTATION
        elif (action_a and action_b) == "C":
            return_a, return_b = self.REWARD, self.REWARD
        else:
            assert False  # "Error, impossible move"

        # state = history
        # state, action, reward, new_state
        self.data[1].append(return_a)
        self.data[2].append(return_b)

        # history, action, return_a, history
        self.prisoner1.punish(state=self.data[1][:-1], action=action_a, reward=return_a, new_state=self.data[1])
        self.prisoner2.punish(state=self.data[2][:-1], action=action_b, reward=return_b, new_state=self.data[2])
