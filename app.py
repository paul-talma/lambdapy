from flask import Flask, request, render_template
from main.run import interpret

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/evaluate", methods=["POST"])
def evaluate():
    expression = request.form["expression"]
    result = interpret(expression)
    return result


if __name__ == "__main__":
    app.run(debug=True)
