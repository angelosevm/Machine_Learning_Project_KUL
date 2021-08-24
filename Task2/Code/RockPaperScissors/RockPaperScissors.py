import numpy as np


class RockPaperScissors:

    def __init__(self, player_b, player_a):
        self.player_b = player_b
        self.player_a = player_a
        self.trajectory = {"player_a": [], "player_b": []}
        self.WIN = 1
        self.LOSE = 0

    def play(self, number_of_games=1):
        for _ in range(number_of_games):
            self.play_one_game()

    def play_one_game(self):
        # Retrieve the actions of each player for this round
        action_player_a, probability_a = self.player_a.choose_action(state=None)
        action_player_b, probability_b = self.player_b.choose_action(state=None)
        self.trajectory["player_a"].append(np.asarray(probability_a))
        self.trajectory["player_b"].append(np.asarray(probability_b))

        # Decide which player wins this round
        if action_player_a == 'R' and action_player_b == 'S' \
                or action_player_a == 'S' and action_player_b == 'P' \
                or action_player_a == 'P' and action_player_b == 'R':
            reward_player_a = self.WIN
            reward_player_b = self.LOSE
        elif action_player_a == 'S' and action_player_b == 'R' \
                or action_player_a == 'P' and action_player_b == 'S' \
                or action_player_a == 'R' and action_player_b == 'P':
            reward_player_a = self.LOSE
            reward_player_b = self.WIN
        else:
            reward_player_a = self.LOSE
            reward_player_b = self.LOSE

        # The outcome of the last round allows both players to learn from it
        self.player_a.learn(state=None,
                            agent_action=action_player_a,
                            opp_action=action_player_b,
                            reward=reward_player_a,
                            new_state=None)
        self.player_b.learn(state=None,
                            agent_action=action_player_b,
                            opp_action=action_player_a,
                            reward=reward_player_b,
                            new_state=None)

