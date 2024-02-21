# utils.py
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.utils import to_categorical

def load_and_preprocess_data():
    # Load Fashion MNIST dataset
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

    # Flatten the images
    X_train = X_train.reshape((X_train.shape[0], -1))
    X_test = X_test.reshape((X_test.shape[0], -1))

    # Normalize the images
    X_train = X_train / 255
    X_test = X_test / 255

    # Convert labels to categorical
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    return X_train, y_train, X_test, y_test