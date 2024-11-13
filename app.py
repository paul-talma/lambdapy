from flask import Flask, request, render_template, redirect, url_for, session
from main.run import parse, interpret, transpile

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
    input_tree = parse(expression)  # generate input tree
    latex_input = transpile(input_tree)  #  generate latex code for input representation
    output_tree = interpret(input_tree)  # interpret expression
    latex_output = transpile(
        output_tree
    )  # generate latex code for output representation

    session["history"].append(
        {
            "expression": expression,
            "latex_input": latex_input,
            "latex_output": latex_output,
        }
    )
    session.modified = True

    return redirect(url_for("index"))


@app.route("/clear_history", methods=["POST"])
def clear_history():
    session["history"] = []
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
