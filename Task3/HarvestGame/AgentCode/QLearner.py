import random
import numpy as np
from Model import Model
import logging
logger = logging.getLogger(__name__)


class QLearner:

    def __init__(self,
                 model=Model(),
                 max_memory=50000,
                 discount=0.9,
                 epsilon=0.1,
                 number_actions=4,
                 epsilon_min=0.01,
                 epsilon_decay=0.99,
                 batch_size=5000):
        self.memory = []
        self.max_memory = max_memory
        self.discount = discount
        self.epsilon = epsilon
        self.actions = list(range(0, number_actions))
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.batch_size = batch_size
        self.model = model

    def save_experience(self, state, action, reward, next_state, game_over):
        # Store <s, a, r, s', game_over?> tuples for the sake of replaying them during training
        self.memory.append((state, action, reward, next_state, game_over))
        if len(self.memory) > self.max_memory:
            del self.memory[0]

    def learn(self):
        print("Training...")
        # Extract a batch from the memory to train on
        batch_x = random.sample(self.memory, min(self.batch_size, len(self.memory)))
        loss_score = 0
        number = 0
        # Loop through every batch experience
        for state, action, reward, next_state, game_over in batch_x:
            if state is not None and not np.any(np.isnan(state)):
                target_best_action = reward
                if not game_over:
                    target_best_action = reward + self.discount * np.max(self.model.predict(next_state)[0])
                target_all_actions = self.model.predict(state)
                # Correct the target for all actions by replacing its values for 'action' with target_best_action
                number += 1
                target_all_actions[0][action] = target_best_action
                history = self.model.fit(state, target_all_actions)
                loss_score += list(history.history.values())[0][0]
        # Save the weights after the training procedure
        self.model.save_weights()
        final_loss = loss_score/len(batch_x)
        print("End of training, loss: " + str(final_loss))
        # Update the value of epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        return final_loss, self.epsilon

    def choose_action(self, state):
        if np.random.rand() <= self.epsilon:
            return random.choice(self.actions)
        return np.argmax(self.model.predict(state)[0])

