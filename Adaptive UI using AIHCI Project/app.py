from flask import Flask, render_template, request

app = Flask(__name__)

training_data = {
    "workday compensation": [
        "Advanced Compensation Configuration",
        "Workday Integrations",
        "Security Administration",
        "AI for HR Professionals"
    ],
    "workday recruiting": [
        "Advanced Recruiting",
        "Talent Analytics",
        "Interview Management",
        "Leadership Development"
    ],
    "python": [
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing",
        "Advanced Python"
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():

    skill = request.form.get("skill", "").lower()

    recommendations = training_data.get(
        skill,
        ["No recommendations found"]
    )

    return render_template(
        "index.html",
        skill=skill,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)