from Learner.MCPILearner import MCIPLearner
from Pennies import Gambler, MatchingPennies
from Learner.QLearner import QLearner
from Learner.NonLearner import NonLearner

import csv
import matplotlib.pyplot as plt

observation_size_a = 4
observation_size_b = 4
epsilon = 0.1
decay = 0.9
even = Gambler.Gambler("A", MCIPLearner("A", decay=decay, epsilon=epsilon, observation_size=observation_size_a, percentage=90))
odd = Gambler.Gambler("B", MCIPLearner("B", decay=decay, epsilon=epsilon, observation_size=observation_size_b, percentage=10))


def analyse_result(list_a, list_b, result_a, result_b):
    for i in range(len(list_a)):
        if list_a[i] == "H":
            result_a[i] += 1
        if list_b[i] == "H":
            result_b[i] += 1
    return result_a, result_b


def training(nb_of_play=100, nb_of_train=10):
    print("Start a non-iterated game between two MachineLearning bots")
    result_a, result_b = [0] * nb_of_play, [0] * nb_of_play
    for _ in range(nb_of_train):
        game = MatchingPennies.MatchingPennies(even=even, odd=odd)
        game.play(nb_of_play)
        result_a, result_b = analyse_result(even.actions, odd.actions, result_a, result_b)
        even.reset()
        odd.reset()
    result_a = [x / nb_of_train for x in result_a]
    result_b = [x / nb_of_train for x in result_b]
    plt.plot(result_a)
    plt.plot(result_b)
    plt.axis([0, nb_of_play, 0, 1])
    plt.show()
    return result_a, result_b


def main():
    nb_play = 2000
    nb_of_train = 1000
    a, b = training(nb_play, nb_of_train)
    with open(f'pennies_{str(even)}{observation_size_a}_{str(odd)}{observation_size_b}.csv', 'w', newline='') as out_f:
        w = csv.writer(out_f)
        w.writerow(range(1, nb_play+1))
        w.writerow(a)
        w.writerow(b)


if __name__ == '__main__':
    main()
