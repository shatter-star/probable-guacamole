# predict.py
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from utils import load_and_preprocess_data
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.utils import to_categorical

# Load the trained model
model = load_model('./models/model.h5')

# Load and preprocess the Fashion MNIST data
_, _, X_test, y_test = load_and_preprocess_data()

# Select a random sample from the test set
random_index = np.random.randint(0, len(X_test))
new_sample = X_test[random_index].reshape(1, -1)

# Use the model to make a prediction
prediction = model.predict(new_sample)
predicted_class = np.argmax(prediction)

# Define the class names of the Fashion MNIST dataset
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Print the predicted and actual class
print(f'The predicted class for the new sample is: {class_names[predicted_class]}')
print(f'The actual class for the new sample is: {class_names[np.argmax(y_test[random_index])]}')

y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_test_classes = np.argmax(y_test, axis=1)

# Calculate metrics
accuracy = accuracy_score(y_test_classes, y_pred_classes)
precision = precision_score(y_test_classes, y_pred_classes, average='macro')
recall = recall_score(y_test_classes, y_pred_classes, average='macro')
f1 = f1_score(y_test_classes, y_pred_classes, average='macro')

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')

# Visualize the new sample
new_sample_image = new_sample.reshape(28, 28)
plt.imshow(new_sample_image, cmap='gray')
plt.title(f'Predicted: {class_names[predicted_class]}\nActual: {class_names[np.argmax(y_test[random_index])]}')
plt.show()