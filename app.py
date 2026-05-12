from flask import Flask, render_template, request
from food_agent import food_ai_agent

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        query = request.form["query"]
        response = food_ai_agent(query)

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)
