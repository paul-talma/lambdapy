from flask import Flask, request, render_template, redirect, url_for, session
from main.run import interpret

app = Flask(__name__)
app.secret_key = "secretsecret"


@app.before_request
def initialize_history():
    if "history" not in session:
        session["history"] = []


@app.route("/")
def index():
    return render_template("index.html", history=session["history"])


@app.route("/evaluate", methods=["POST"])
def evaluate():
    expression = request.form["expression"]
    result = interpret(expression)

    session["history"].append({"expression": expression, "result": result})
    session.modified = True

    return redirect(url_for("index"))


@app.route("/clear_history", methods=["POST"])
def clear_history():
    session["history"] = []
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
