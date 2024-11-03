from flask import Flask, request, render_template
from main.run import interpret

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", result=None)


@app.route("/evaluate", methods=["POST"])
def evaluate():
    expression = request.form["expression"]
    result = interpret(expression)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
