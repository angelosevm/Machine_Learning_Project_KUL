from keras import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint


class Model:

    def __init__(self,
                 input_size=50,
                 number_of_actions=4,
                 learning_rate=1e-6,
                 weights_path="./modelweights/weights.h5",
                 learn_from_scratch=True):
        self.model = Sequential()
        self.model.add(Dense(64, input_dim=input_size, activation='relu'))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(number_of_actions, activation='linear'))
        adam = Adam(lr=learning_rate)
        self.model.compile(optimizer=adam, loss='mse', metrics=['accuracy'])

        # Callback for intermediate saves between epochs (saving updated weights)
        self.weights_path = weights_path
        checkpoint = ModelCheckpoint(self.weights_path, monitor=["loss"], verbose=1, mode='max')
        self.callbacks_list = [checkpoint]

        if not learn_from_scratch:
            self.model.load_weights(self.weights_path)

    def predict(self, state):
        return self.model.predict(state)

    def fit(self, X, Y):
        return self.model.fit(X, Y, epochs=1, verbose=0)

    def save_weights(self, path="./modelweights/weights.h5"):
        self.model.save_weights(path)

    def summary(self):
        self.model.summary()
