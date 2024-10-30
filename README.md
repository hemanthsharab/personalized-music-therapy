# Personalized Music Therapy Using Deep Learning

## Project Overview
A web application that recommends therapeutic music based on mood. It analyzes audio features and predicts the mood to provide tailored music recommendations.

## Setup

1. Clone the repository and navigate into the project directory.
    ```bash
    git clone https://github.com/your-username/personalized-music-therapy.git
    cd personalized-music-therapy
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Train the model (optional):
    ```bash
    python app/model.py
    ```

4. Run the web application:
    ```bash
    python run.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000`.

## Usage
- Upload an audio file, and the system will analyze its mood.
- The app will suggest music based on the detected mood.

## Files

- **app/model.py**: Model training script.
- **app/recommender.py**: Audio feature extraction and mood prediction.
- **app/main.py**: Flask application routes.

## Dataset
Use your own labeled dataset of music audio files with moods.
