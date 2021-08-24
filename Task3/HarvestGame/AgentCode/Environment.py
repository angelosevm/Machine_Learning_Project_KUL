import numpy as np
import logging
logger = logging.getLogger(__name__)


class Environment:

    def __init__(self, number_of_rows=36, number_of_columns=16, input_size=50):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.input_size = input_size
        self.pre_response_messages = {}

    def update_rows_and_columns(self, number_of_rows, number_of_columns):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns

    def preprocess_state(self, message):
        if message['type'] == 'start':
            agent_id = message['player']
        else:
            agent_id = message['nextplayer']
        # Pre-response messages are used later on by the environment to be compared to the post-response messages
        self.pre_response_messages[agent_id] = message

        apples = message['apples']
        agent = message['players'][agent_id-1]

        # Distance to the closest apple
        closest_apple_distance = self.distance_to_closest_apple(apples, agent['location']) / 7

        # Number of apples in 15 x 15 area
        number_of_apples = len(apples) / (15*15)

        # Number of enemies on 15x15 screen (start at -1 to compensate for counting the agent)
        number_of_enemies = -1
        # Is the agent currently winning?
        all_players = message['players']
        currently_winning = 1
        for player in all_players:
            if not message['type'] == 'start' and player['score'] > agent['score']:
                currently_winning = 0
            if not player['orientation'] == '?':
                number_of_enemies += 1

        apple_right_in_front = self.apple_right_in_front(agent, apples)
        apple_to_the_left = self.apple_to_the_left(agent, apples)
        apple_to_the_right = self.apple_to_the_right(agent, apples)

        number_of_enemies /= len(all_players)
        # Is an enemy in front of the agent?
        enemy_in_front = self.enemy_in_front(all_players, agent)
        enemy_behind = self.enemy_behind(all_players, agent)
        enemy_to_the_left = self.enemy_to_the_left(all_players, agent)
        enemy_to_the_right = self.enemy_to_the_right(all_players, agent)
        state = np.zeros((1, self.input_size))

        # Creating the feature vector
        state[0][0] = (self.distance_to_closest_apple_in_front(apples, agent) / 7) * 0.5
        state[0][1] = (self.distance_to_closest_apple_left(apples, agent) / 7) * 0.5
        state[0][2] = (self.distance_to_closest_apple_right(apples, agent) / 7) * 0.5
        state[0][3] = number_of_enemies
        state[0][4] = currently_winning * 2
        state[0][5] = enemy_in_front
        state[0][6] = number_of_apples
        state[0][7] = apple_right_in_front * 3.5
        state[0][8] = apple_to_the_left * 3.5
        state[0][9] = apple_to_the_right * 3.5
        state[0][10] = enemy_behind
        state[0][11] = enemy_to_the_left
        state[0][12] = enemy_to_the_right

        return state

    def extract_environment_response(self, environment_response_message, action):
        # Extracting the environment response from an environment response message

        pre_response_message = self.pre_response_messages[environment_response_message['nextplayer']]

        if environment_response_message['type'] == 'start':
            agent_id = environment_response_message['player']
        else:
            agent_id = environment_response_message['nextplayer']

        reward = 0

        agent_post_response = environment_response_message['players'][agent_id-1]
        agent_pre_response = pre_response_message['players'][agent_id - 1]

        if pre_response_message['type'] == 'start':
            pre_response_score = 0
        else:
            pre_response_score = agent_pre_response['score']

        # Adding score increase to the reward
        reward += (agent_post_response['score'] - pre_response_score)

        if reward == 0 and action == 'fire':
            reward -= 1
        next_state = self.preprocess_state(environment_response_message)
        return reward, next_state, False

    @staticmethod
    def extract_end_game_response(message, player, state):
        if message['winner'] == player:
            reward = 100
        else:
            reward = -100
        return reward, state, True

    @staticmethod
    def distance_to_closest_apple(apples, agent_location):
        closest_distance = np.infty
        for apple in apples:
            # Euclidean distance
            distance = np.linalg.norm(np.asarray(apple, dtype='int32') - np.asarray(agent_location, dtype='int32'))
            if distance < closest_distance:
                closest_distance = distance
        if closest_distance == np.infty:
            return 7
        return closest_distance

    @staticmethod
    def distance_to_closest_apple_in_front(apples, agent):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']
        for apple in apples:
            if agent_orientation == 'up':
                for i in range(1, 8):
                    if apple == [x, y - i]:
                        return i
            elif agent_orientation == 'down':
                for i in range(1, 8):
                    if apple == [x, y + i]:
                        return i
            elif agent_orientation == 'left':
                for i in range(1, 8):
                    if apple == [x - i, y]:
                        return i
            elif agent_orientation == 'right':
                for i in range(1, 8):
                    if apple == [x + i, y]:
                        return i
        return 7

    @staticmethod
    def distance_to_closest_apple_right(apples, agent):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']
        for apple in apples:
            if agent_orientation == 'up':
                for i in range(1, 8):
                    if apple == [x+i, y]:
                        return i
            elif agent_orientation == 'down':
                for i in range(1, 8):
                    if apple == [x-i, y]:
                        return i
            elif agent_orientation == 'left':
                for i in range(1, 8):
                    if apple == [x, y-i]:
                        return i
            elif agent_orientation == 'right':
                for i in range(1, 8):
                    if apple == [x, y+i]:
                        return i
        return 7

    @staticmethod
    def distance_to_closest_apple_left(apples, agent):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']
        for apple in apples:
            if agent_orientation == 'up':
                for i in range(1, 8):
                    if apple == [x-i, y]:
                        return i
            elif agent_orientation == 'down':
                for i in range(1, 8):
                    if apple == [x+i, y]:
                        return i
            elif agent_orientation == 'left':
                for i in range(1, 8):
                    if apple == [x, y+i]:
                        return i
            elif agent_orientation == 'right':
                for i in range(1, 8):
                    if apple == [x, y-i]:
                        return i
        return 7

    def enemy_in_front(self, enemies, agent):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']

        for enemy in enemies:
            enemy_location = enemy['location']
            if agent_orientation == 'up':
                for i in range(1, self.number_of_columns):
                    if enemy_location == [x, y-i]:
                        return 1
            elif agent_orientation == 'down':
                for i in range(1, self.number_of_columns):
                    if enemy_location == [x, y+i]:
                        return 1
            elif agent_orientation == 'left':
                for i in range(1, self.number_of_rows):
                    if enemy_location == [x-i, y]:
                        return 1
            elif agent_orientation == 'right':
                for i in range(1, self.number_of_rows):
                    if enemy_location == [x+i, y]:
                        return 1
        return 0

    def enemy_behind(self, enemies, agent):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']

        for enemy in enemies:
            enemy_location = enemy['location']
            if agent_orientation == 'up':
                for i in range(1, self.number_of_columns):
                    if enemy_location == [x, y+i]:
                        return 1
            elif agent_orientation == 'down':
                for i in range(1, self.number_of_columns):
                    if enemy_location == [x, y-i]:
                        return 1
            elif agent_orientation == 'left':
                for i in range(1, self.number_of_rows):
                    if enemy_location == [x+i, y]:
                        return 1
            elif agent_orientation == 'right':
                for i in range(1, self.number_of_rows):
                    if enemy_location == [x-i, y]:
                        return 1
        return 0

    def enemy_to_the_left(self, enemies, agent):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']

        for enemy in enemies:
            enemy_location = enemy['location']
            if agent_orientation == 'up':
                for i in range(1, self.number_of_columns):
                    if enemy_location == [x-i, y]:
                        return 1
            elif agent_orientation == 'down':
                for i in range(1, self.number_of_columns):
                    if enemy_location == [x+i, y]:
                        return 1
            elif agent_orientation == 'left':
                for i in range(1, self.number_of_rows):
                    if enemy_location == [x, y+i]:
                        return 1
            elif agent_orientation == 'right':
                for i in range(1, self.number_of_rows):
                    if enemy_location == [x, y-i]:
                        return 1
        return 0

    def enemy_to_the_right(self, enemies, agent):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']

        for enemy in enemies:
            enemy_location = enemy['location']
            if agent_orientation == 'up':
                for i in range(1, self.number_of_columns):
                    if enemy_location == [x+i, y]:
                        return 1
            elif agent_orientation == 'down':
                for i in range(1, self.number_of_columns):
                    if enemy_location == [x-i, y]:
                        return 1
            elif agent_orientation == 'left':
                for i in range(1, self.number_of_rows):
                    if enemy_location == [x, y-i]:
                        return 1
            elif agent_orientation == 'right':
                for i in range(1, self.number_of_rows):
                    if enemy_location == [x, y+i]:
                        return 1
        return 0

    @staticmethod
    def apple_right_in_front(agent, apples):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']

        for apple in apples:
            if agent_orientation == 'up':
                if apple == [x, y - 1]:
                    return 1
            elif agent_orientation == 'down':
                if apple == [x, y + 1]:
                    return 1
            elif agent_orientation == 'left':
                if apple == [x - 1, y]:
                    return 1
            elif agent_orientation == 'right':
                if apple == [x + 1, y]:
                    return 1
        return 0

    @staticmethod
    def apple_to_the_left(agent, apples):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']

        for apple in apples:
            if agent_orientation == 'up':
                if apple == [x - 1, y]:
                    return 1
            elif agent_orientation == 'down':
                if apple == [x + 1, y]:
                    return 1
            elif agent_orientation == 'left':
                if apple == [x, y + 1]:
                    return 1
            elif agent_orientation == 'right':
                if apple == [x, y - 1]:
                    return 1
        return 0

    @staticmethod
    def apple_to_the_right(agent, apples):
        [x, y] = agent['location']
        agent_orientation = agent['orientation']

        for apple in apples:
            if agent_orientation == 'up':
                if apple == [x + 1, y]:
                    return 1
            elif agent_orientation == 'down':
                if apple == [x - 1, y]:
                    return 1
            elif agent_orientation == 'left':
                if apple == [x, y - 1]:
                    return 1
            elif agent_orientation == 'right':
                if apple == [x, y + 1]:
                    return 1
        return 0
