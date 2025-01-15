from flask import Flask, render_template, request, redirect, url_for

from generator import Generator, StrategyA

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

        mstrategy = StrategyA()
        mgenerator = Generator(mstrategy)
        mgenerator.s = int(form_s)
        mgenerator.n = int(form_n)
        mgenerator.generate(int(form_size))

        return redirect(url_for("result", size=form_size))
    else:
        return render_template("generate.html")


@app.route("/result/<size>")
def result(size):
    return render_template("result.html", result=size)


if __name__ == "__main__":
    app.run(debug=True)
