from QLearner import QLearner
from FictitiousLearner import FictitiousLearner
from QFictitiousLearner import QFictitiousLearner
from Player import Player
from RockPaperScissors import RockPaperScissors
import numpy as np
from TernaryLearningCurves import TernaryLearningCurves

observation_size = 1
learning_rate = 0.0005
decay = 0.9
epsilon = 0.1
number_of_games = 1000
number_of_players_per_game = 1
temperature = 1
normalization_constant = 1000


def scenario(number=1):
    if number < 5:
        player_a1 = Player("A", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[90, 5, 5]))
        player_a2 = Player("A", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 90, 5]))
        player_a3 = Player("A", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 5, 90]))
    elif number < 9:
        player_a1 = Player("A", QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[90, 5, 5]))
        player_a2 = Player("A", QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[5, 90, 5]))
        player_a3 = Player("A", QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[5, 5, 90]))

    else:
        player_a1 = Player("A", FictitiousLearner(strategy_layout=[90, 5, 5]))
        player_a2 = Player("A", FictitiousLearner(strategy_layout=[5, 90, 5]))
        player_a3 = Player("A", FictitiousLearner(strategy_layout=[5, 5, 90]))

    if number == 1:
        player_b1 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[33, 33, 34]))
        player_b2 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[33, 33, 34]))
        player_b3 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[33, 33, 34]))
    elif number == 2:
        player_b1 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[90, 5, 5]))
        player_b2 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 90, 5]))
        player_b3 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 5, 90]))
    elif number == 3:
        player_b1 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 5, 90]))
        player_b2 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[90, 5, 5]))
        player_b3 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 90, 5]))
    elif number == 4:
        player_b1 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=0, strategy_layout=[33, 33, 34]))
        player_b2 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=0, strategy_layout=[33, 33, 34]))
        player_b3 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=0, strategy_layout=[33, 33, 34]))
    elif number == 5:
        player_b1 = Player("B", QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[90, 5, 5]))
        player_b2 = Player("B", QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[5, 90, 5]))
        player_b3 = Player("B", QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[5, 5, 90]))
    elif number == 6:
        player_b1 = Player("B", FictitiousLearner(strategy_layout=[90, 5, 5]))
        player_b2 = Player("B", FictitiousLearner(strategy_layout=[5, 90, 5]))
        player_b3 = Player("B", FictitiousLearner(strategy_layout=[5, 5, 90]))
    elif number == 7:
        player_b1 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[90, 5, 5]))
        player_b2 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 90, 5]))
        player_b3 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 5, 90]))
    elif number == 8:
        player_b1 = Player("B",
                           QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[5, 90, 5]))
        player_b2 = Player("B",
                           QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[5, 5, 90]))
        player_b3 = Player("B",
                           QFictitiousLearner(decay=decay, learning_rate=learning_rate, strategy_layout=[90, 5, 5]))
    elif number == 9:
        player_b1 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[90, 5, 5]))
        player_b2 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 90, 5]))
        player_b3 = Player("B", QLearner(decay=decay, temperature=temperature, normalization_constant=normalization_constant, learning_rate=learning_rate, strategy_layout=[5, 5, 90]))

    else:
        player_b1 = Player("B", FictitiousLearner(strategy_layout=[90, 5, 5]))
        player_b2 = Player("B", FictitiousLearner(strategy_layout=[5, 90, 5]))
        player_b3 = Player("B", FictitiousLearner(strategy_layout=[5, 5, 90]))

    return player_a1, player_a2, player_a3, player_b1, player_b2, player_b3


def training(player_a, player_b):
    print("Training...")
    results_a, results_b = np.zeros((number_of_games, 3)), np.zeros((number_of_games, 3))
    for _ in range(number_of_players_per_game):
        game = RockPaperScissors(player_a=player_a, player_b=player_b)
        game.play(number_of_games)
        results_a = game.trajectory['player_a']
        results_b = game.trajectory['player_b']
        player_a.reset()
        player_b.reset()
    results_a = [x / number_of_players_per_game for x in results_a]
    results_b = [x / number_of_players_per_game for x in results_b]
    return results_a, results_b


def main():
    player_a1, player_a2, player_a3, player_b1, player_b2, player_b3 = scenario(10)
    results_a1, results_b1 = training(player_a1, player_b1)
    results_a2, results_b2 = training(player_a2, player_b2)
    results_a3, results_b3 = training(player_a3, player_b3)
    TernaryLearningCurves.plot_curves(curves=[results_a1, results_a2, results_a3], name="player_a")
    TernaryLearningCurves.plot_curves(curves=[results_b1, results_b2, results_b3], name="player_b")
    TernaryLearningCurves.plot_theoretical_trajectory()


if __name__ == '__main__':
    main()
