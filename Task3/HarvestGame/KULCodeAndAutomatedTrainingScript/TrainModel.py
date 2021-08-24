import os
import random
import time

number_of_iterations = 40
for i in range(number_of_iterations):
    n_apples = random.randint(1, 5)
    n_apples = 3
    localhost_nb = random.randint(2, 8)
    localhost_nb = 4

    with open('../AgentCode/scores.txt', 'a') as file:
        file.write("Iteration " + str(i+1) + '\n')
    command = "node play.js "
    for i in range(localhost_nb):
        command += "ws://localhost:8889 "
    command += str(n_apples)
    os.system(command)
    time.sleep(15)

