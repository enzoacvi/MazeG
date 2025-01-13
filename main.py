from flask import Flask, render_template, request, redirect, url_for
from logic import maze_generator, strategies
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        redirect(url_for("generate"))
    else:
        return render_template("home.html")


@app.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        form_size = request.form["size"]
        form_s = request.form["s"]
        form_n = request.form["n"]
        # recibir del form los factores s, n
        mgenerator.generate(form_size)
        mgenerator.s = form_s
        mgenerator.n = form_n
        return redirect(url_for("result", size=form_size))
    else:
        return render_template("generate.html")


@app.route("/result/<size>")
def result(size):
    return render_template("result.html", result=size)


if __name__ == "__main__":
    app.run(debug=True)
    mstrategy = strategies.StrategyA()
    # Tengo que pasarle el size al mgenerator
    mgenerator = maze_generator.Generator(mstrategy)
