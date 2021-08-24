class MatchingPennies:

    def __init__(self, odd, even):
        self.odd = odd
        self.even = even
        self.data = {"odd": [], "even": []}

        self.WIN = 1
        self.LOSE = 0

    def play(self, move=1):
        for _ in range(move):
            self.play_a_move()

    def play_a_move(self):
        """
        Execute one iteration of the game
        We ask for strategy and then save the results
        """
        # The state here is the history of the player results
        action_even = self.even.strategy(state=self.data["even"])
        action_odd = self.odd.strategy(state=self.data["odd"])

        if action_even == action_odd == "H" or action_even == action_odd == "T":
            return_even = self.WIN
            return_odd = self.LOSE
        else:
            return_even = self.LOSE
            return_odd = self.WIN

        # state = history
        # state, action, reward, new_state
        self.data["even"].append(return_even)
        self.data["odd"].append(return_odd)

        # history, action, return_a, history
        self.even.punish(state=self.data["even"][:-1],
                         action=action_even,
                         reward=return_even,
                         new_state=self.data["even"])
        self.odd.punish(state=self.data["odd"][:-1],
                        action=action_odd,
                        reward=return_odd,
                        new_state=self.data["odd"])

