from flask import Flask, request, render_template
from main.run import interpret

app = Flask(__name__)

history = []


@app.route("/")
def index():
    return render_template("index.html", history=history)


@app.route("/evaluate", methods=["POST"])
def evaluate():
    expression = request.form["expression"]
    result = interpret(expression)

    history.append({"expression": expression, "result": result})

    return render_template("index.html", history=history)


if __name__ == "__main__":
    app.run(debug=True)
