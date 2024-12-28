from flask import Flask, request, render_template, redirect, url_for, session
from main.run import parse, interpret, transpile
from main.parser import ParserError

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
    try:
        input_tree = parse(expression)  # generate input tree
        latex_input = transpile(
            input_tree
        )  # generate latex code for input representation
        output_tree = interpret(input_tree)  # interpret expression
        latex_output = transpile(
            output_tree
        )  # generate latex code for output representation

        result = {
            "expression": expression,
            "latex_input": latex_input,
            "latex_output": latex_output,
        }

        session["history"].append(result)
        session.modified = True
        return redirect(url_for("index"))

    except ParserError as e:
        app.logger.error(f"Error message: {e}.\n")
        return render_template("index.html", history=session["history"], error=str(e))
    except RecursionError:
        return render_template(
            "index.html", history=session["history"], error="Nice try ;)"
        )


@app.route("/clear_history", methods=["POST"])
def clear_history():
    session["history"] = []
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
