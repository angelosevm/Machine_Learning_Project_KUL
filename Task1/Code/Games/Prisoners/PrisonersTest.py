from Prisoners import Prisoner
from Prisoners import PrisonerDilemma
from Learner.QLearner import QLearner
from Learner.NonLearner import NonLearner
from Learner.MCPILearner import MCIPLearner
import csv
import matplotlib.pyplot as plt

# For NonLearner 0 = defect, 1 = coop
observation_size_a = 4
observation_size_b = 4
epsilon = 0.06
decay = 0.68
prisoner_a = Prisoner.Prisoner("A", MCIPLearner("A", decay=decay, epsilon=epsilon, observation_size=observation_size_a, percentage=60))
prisoner_b = Prisoner.Prisoner("B", MCIPLearner("B", decay=decay, epsilon=epsilon, observation_size=observation_size_b, percentage=20))


def analyse_result(list_a, list_b, result_a, result_b):
    for i in range(len(list_a)):
        if list_a[i] == "D":
            result_a[i] += 1
        if list_b[i] == "D":
            result_b[i] += 1
    return result_a, result_b


def training(nb_of_play=100, nb_of_train=10):
    print("Start")
    result_a, result_b = [0] * nb_of_play, [0] * nb_of_play
    for _ in range(nb_of_train):
        game = PrisonerDilemma.PrisonerDilemma(prisoner_a, prisoner_b)
        game.play(nb_of_play)
        result_a, result_b = analyse_result(prisoner_a.actions, prisoner_b.actions, result_a, result_b)
        prisoner_a.reset()
        prisoner_b.reset()
    result_a = [x / nb_of_train for x in result_a]
    result_b = [x / nb_of_train for x in result_b]
    plt.plot(result_a)
    plt.plot(result_b)
    plt.show()
    return result_a, result_b


def main():
    nb_play = 1500
    nb_of_train = 1000
    a, b = training(nb_play, nb_of_train)
    with open(f'prisoners_{str(prisoner_a)}{observation_size_a}_{str(prisoner_b)}{observation_size_b}.csv', 'w', newline='') as out_f:
        w = csv.writer(out_f)
        w.writerow(range(1, nb_play+1))
        w.writerow(a)
        w.writerow(b)


if __name__ == '__main__':
    main()
