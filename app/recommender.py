import librosa
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained model
mood_model = load_model('models/mood_model.h5')

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=30)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return np.mean(mfcc.T, axis=0)

def predict_mood(file_path):
    features = extract_features(file_path).reshape(1, -1)
    mood_prediction = mood_model.predict(features)
    moods = ['Happy', 'Sad', 'Relaxed', 'Energetic']
    return moods[np.argmax(mood_prediction)]
