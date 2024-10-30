import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data():
    # Load data and labels
    data = np.load("data/features.npy")
    labels = np.load("data/labels.npy")

    # Encode labels
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)
    return train_test_split(data, labels, test_size=0.2, random_state=42)

def create_model(input_shape):
    model = Sequential([
        Dense(256, activation='relu', input_shape=(input_shape,)),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dense(4, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    X_train, X_test, y_train, y_test = load_data()
    model = create_model(X_train.shape[1])
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=32)
    model.save("models/mood_model.h5")
