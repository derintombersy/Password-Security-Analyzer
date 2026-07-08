from flask import Flask, render_template, request
from analyzer import analyze_password, generate_strong_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    generated_password = generate_strong_password()

    if request.method == "POST":
        password = request.form["password"]

        score, strength, suggestions, percent = analyze_password(password)

        result = {
            "password": password,
            "score": score,
            "strength": strength,
            "percent": percent,
            "suggestions": suggestions
        }

    return render_template(
        "index.html",
        result=result,
        generated_password=generated_password
    )


if __name__ == "__main__":
    app.run(debug=True)
    