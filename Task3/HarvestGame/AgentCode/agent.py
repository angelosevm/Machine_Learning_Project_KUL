#!/usr/bin/env python3
# encoding: utf-8

import sys
import argparse
import logging
import asyncio
import websockets
import json
from Model import Model
from Environment import Environment
from QLearner import QLearner

logger = logging.getLogger(__name__)
games = {}
agentclass = None

input_size = 13
model = Model(input_size, 4, learn_from_scratch=True, learning_rate=5e-6, weights_path="./modelweights/weights.h5")
learner = QLearner(model, max_memory=50000, discount=0.85, epsilon=0.9, number_actions=4, epsilon_decay=0.9, epsilon_min=0.01)
environment = Environment(input_size=input_size)


class Agent:

    def __init__(self, player, number_of_rows, number_of_columns):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.player = {player}
        self.ended = False
        self.actions = {0: 'move', 1: 'left', 2: 'right', 3: 'fire'}
        self.actions_number = {'move': 0, 'left': 1, 'right': 2, 'fire': 3}
        self.current_player_configurations = {player: ('move', None)}
        environment.update_rows_and_columns(number_of_rows=number_of_rows, number_of_columns=number_of_columns)

    def add_player(self, player):
        # The same Agent may be used for several players
        self.player.add(player)
        self.current_player_configurations[player] = ('move', None)

    def next_action(self, state):
        action = learner.choose_action(state)
        return self.actions[action]

    def register_action(self, environment_response_message):
        # Save a new experience <s, a, r, s', game_over>
        current_action = self.current_player_configurations[environment_response_message['nextplayer']][0]
        current_state = self.current_player_configurations[environment_response_message['nextplayer']][1]
        action_number = self.actions_number[current_action]
        reward, next_state, game_over = environment.extract_environment_response(environment_response_message, current_action)
        learner.save_experience(current_state, action_number, reward, next_state, game_over)

    def end_game(self, message):
        # Learning takes place after the end of a game
        loss = 0
        epsilon = 0
        for p in self.player:
            current_action = self.current_player_configurations[p][0]
            current_state = self.current_player_configurations[p][1]
            action_number = self.actions_number[current_action]
            reward, next_state, game_over = environment.extract_end_game_response(message, p, current_state)
            learner.save_experience(current_state, action_number, reward, next_state, game_over)
        if not self.ended:
            loss, epsilon = learner.learn()
        self.ended = True
        self.save_statistics(message, loss, epsilon)

    def new_game(self):
        self.ended = False

    def save_current_player_configuration(self, state, action, player):
        self.current_player_configurations[player] = (action, state)

    @staticmethod
    def save_statistics(end_message, loss, epsilon):
        # Information about the learning process of the agent is stored in a text file
        scores = []
        with open('scores.txt', 'a') as file:
            players = end_message['players']
            for p in players:
                scores.append(p['score'])
            file.write('Scores : ' + str(scores) + '\n')
            file.write('Loss : ' + str(loss) + '\n')
            file.write('New epsilon : ' + str(epsilon) + '\n')


async def handler(websocket, path):
    logger.info("Start listening")
    try:
        async for msg in websocket:
            #logger.info("< {}".format(msg))
            try:
                msg = json.loads(msg)
            except json.decoder.JSONDecodeError as err:
                logger.error(err)
                return False
            game = msg["game"]
            answer = None
            if msg["type"] == "start":
                if game in games:
                    # Set up a new game with an existing agent
                    games[game].new_game()
                    games[game].add_player(msg["player"])
                else:
                    # Create a new agent and let said agent be reached through the new game
                    number_of_columns, number_of_rows = msg["grid"]
                    games[game] = agentclass(msg["player"], number_of_rows, number_of_columns)
                state = environment.preprocess_state(msg)
                if msg["player"] == 1:
                    # Player 1 is played by the agent and needs to make the first move
                    action = games[game].next_action(state)
                    games[game].save_current_player_configuration(state, action, msg["player"])
                    if action is None:
                        logger.info("Game over")
                        continue
                    answer = {'type': 'action', 'action': action}
                else:
                    answer = None

            elif msg["type"] == "action":
                if msg["nextplayer"] in games[game].player and msg["nextplayer"] == msg["receiver"]:
                    # 'nextplayer', i.e. the player that is making the next move, is controlled by the agent
                    games[game].register_action(msg)
                    state = environment.preprocess_state(msg)
                    action = games[game].next_action(state)
                    games[game].save_current_player_configuration(state, action, msg["nextplayer"])
                    if action is None:
                        logger.info("Game over")
                        continue
                    answer = {'type': 'action', 'action': action}
                else:
                    answer = None

            elif msg["type"] == "end":
                games[game].end_game(msg)
                answer = None
            else:
                logger.error("Unknown message type:\n{}".format(msg))

            if answer is not None:
                await websocket.send(json.dumps(answer))
                #logger.info("> {}".format(answer))
    except websockets.exceptions.ConnectionClosed as err:
        logger.info("Connection closed")
    logger.info("Exit handler")


def start_server(port):
    server = websockets.serve(handler, 'localhost', port)
    print("Running on ws://127.0.0.1:{}".format(port))
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()


def main(argv=None):
    global agentclass
    parser = argparse.ArgumentParser(description='Start agent to play the Apples game')
    parser.add_argument('--verbose', '-v', action='count', default=0, help='Verbose output')
    parser.add_argument('--quiet', '-q', action='count', default=0, help='Quiet output')
    parser.add_argument('port', metavar='PORT', type=int, help='Port to use for server')
    args = parser.parse_args(argv)

    logger.setLevel(max(logging.INFO - 10 * (args.verbose - args.quiet), logging.DEBUG))
    logger.addHandler(logging.StreamHandler(sys.stdout))

    agentclass = Agent
    start_server(args.port)


if __name__ == "__main__":
    sys.exit(main())
