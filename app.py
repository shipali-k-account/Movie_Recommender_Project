from flask import Flask, render_template, request
from recommender import recommend_movies
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    error_message = None
    genre_input = ""

    if request.method == "POST":
        genre_input = request.form["genre"].strip()

        if genre_input:
            recommendations = recommend_movies(genre_input)
        else:
            error_message = "Please enter at least one genre to get recommendations."

    return render_template(
        "index.html",
        recommendations=recommendations,
        error=error_message,
        genre_input=genre_input,
        current_year=datetime.now().year
    )

if __name__ == "__main__":
    app.run(debug=True)
