from flask import Flask, request, render_template
from recommender import predict_mood

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if 'file' not in request.files:
        return "No file provided"
    file = request.files['file']
    file_path = f"data/music/{file.filename}"
    file.save(file_path)

    # Predict mood and display recommendations
    mood = predict_mood(file_path)
    recommendations = get_music_recommendations(mood)
    return render_template('recommend.html', mood=mood, recommendations=recommendations)

def get_music_recommendations(mood):
    # Example recommendation logic
    recommendations = {
        "Happy": ["Happy Song 1", "Happy Song 2"],
        "Sad": ["Sad Song 1", "Sad Song 2"],
        "Relaxed": ["Relaxed Song 1", "Relaxed Song 2"],
        "Energetic": ["Energetic Song 1", "Energetic Song 2"]
    }
    return recommendations.get(mood, [])

if __name__ == '__main__':
    app.run(debug=True)
