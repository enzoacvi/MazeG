from flask import Flask, render_template, request, redirect, url_for

from generator import Generator, StrategyA, StrategyB, StrategyC

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
        form_strategy = request.form["strategy"]

        return redirect(url_for("result", strategy=form_strategy,
                                size=form_size, s=form_s, n=form_n))
    else:
        return render_template("generate.html")


@app.route("/result/<strategy>/<size>/<s>/<n>")
def result(strategy, size, s, n):
    if strategy == '1':
        mstrategy = StrategyA()
    elif strategy == '2':
        mstrategy = StrategyB()
    elif strategy == '3':
        mstrategy = StrategyC()

    mgenerator = Generator(mstrategy)
    mgenerator.s = int(s)
    mgenerator.n = int(n)
    maze_result = mgenerator.generate(int(size))

    return render_template("result.html", result=maze_result)


if __name__ == "__main__":
    app.run(debug=True)
