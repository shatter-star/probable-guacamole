# model.py
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from utils import load_and_preprocess_data

def train_and_save_model():
    # Load and preprocess the data
    X_train, y_train, X_test, y_test = load_and_preprocess_data()

    # Define the model
    model = Sequential()
    model.add(Dense(512, activation='relu', input_dim=784))
    model.add(Dense(10, activation='softmax'))

    # Compile the model
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    history = model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

    # Ensure the file path exists
    if not os.path.exists('./models/'):
        os.makedirs('./models/')

    # Save the trained model to a file
    model.save('./models/model.h5')

if __name__ == "__main__":
    train_and_save_model()