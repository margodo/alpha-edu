import cv2
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Uploading image and making it gray:
image = cv2.imread('example.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Finding face:
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# Drawing rectangle on the face:
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Showing the result:
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# **Задача**: Создание модели, которая будет прогнозировать цену домов на основе их площади.
X = np.array([[50], [70], [100], [120]])
y = np.array([150, 200, 300, 350])

model = LinearRegression().fit(X, y)
price = model.predict([[90]])
print(f"Excpected price for 90sqm house is: {price[0]} thousand $")

plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, model.predict(X), color='red', label='Forecast')
plt.xlabel('Square (sqm)')
plt.ylabel('Price (thousand $)')
plt.title('Expected prices')
plt.legend()
plt.show()