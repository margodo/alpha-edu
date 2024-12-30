import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class  NeuralNetworkExample:

    def __init__(self):
        self.model = None
        self.x_train = None
        self.y_train = None

    def prepare_data(self):
        self.x_train = np.array([[30,1],[50,2],[70,3],[90,4],[120,5]], dtype=np.float32)
        self.y_train = np.array([100,150,200,250,300], dtype=np.float32)
    
    def build_model(self):
        self.model = Sequential([
            Dense(10, input_dim=2, activation ='relu'),
            Dense(1)
        ])
        self.model.complie(optimizer='adam', loss='mean_squared_error')
    
    def train_model(self):
        self.model.fit(self.x_trian, self.y_train, epochs=100, verbose=1)

    def test_model(self):
        x_test = np.array([[40,1],[80,3],[100,4]], dtype=np.float32)
        prediction = self.model.predict(x_test)
        print('Result:')
        for i,pred in enumerate(prediction):
            print(f'Data: {x_test[i]} - prection: {pred[0]:.2f} US dollars.')

if __name__ == "__main__":
    nn_example = NeuralNetworkExample()
    nn_example.prepare_data()
    nn_example.build_model()
    nn_example.train_model()
    nn_example.test_model()