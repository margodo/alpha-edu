import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from random import randint
import matplotlib.pyplot as plt

data = []
prices = []
for i in range(0,100):
    square = randint(20,160)
    if square < 50:
        rooms = randint(1,2)
        price = randint(100,150)
    elif square < 100:
        rooms = randint(3,5)
        price = randint(180,500)
    else:
        rooms = randint(5,8)
        price = randint(550,1000)
    prices.append(price)
    data.append([square, rooms])

class  NeuralNetworkExample:

    def __init__(self):
        self.model = None
        self.x_train = None
        self.y_train = None

    def prepare_data(self):
        self.x_train = np.array(data, dtype=np.float32)
        self.y_train = np.array(prices, dtype=np.float32)
    
    def build_model(self):
        self.model = Sequential([
            Dense(10, input_dim=2, activation ='relu'),
            Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mean_squared_error')
    
    def train_model(self):
        self.model.fit(self.x_train, self.y_train, epochs=100, verbose=1)

    def test_model(self):
        x_test = np.array([[40,1],[80,3],[100,4]], dtype=np.float32)
        prediction = self.model.predict(x_test)
        print('Result:')
        for i,pred in enumerate(prediction):
            print(f'Data: {x_test[i]} - prediction: {pred[0]:.2f} US dollars.')
    
    def plot_predictions(self):
        predicted_prices = self.model.predict(self.x_train)

        plt.figure(figsize=(10,6))
        
        plt.scatter([x[0] for x in self.x_train], self.y_train, color='blue', label='Actual Prices', alpha=0.5)

        plt.scatter([x[0] for x in self.x_train], predicted_prices, color='red', label='Predicted Prices', alpha=0.5)

        plt.title("Actual vs Predicted Apartment Prices")
        plt.xlabel("Apartment Size (m²)")
        plt.ylabel("Price (US Dollars)")
        plt.legend()
        plt.show()
        

if __name__ == "__main__":
    nn_example = NeuralNetworkExample()
    nn_example.prepare_data()
    nn_example.build_model()
    nn_example.train_model()
    nn_example.test_model()
    nn_example.plot_predictions()