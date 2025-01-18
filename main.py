from flask import Flask, render_template, request, redirect, url_for

from generator import Generator, StrategyA, StrategyB, StrategyC

app = Flask(__name__)

strategies = {"Strategy A": StrategyA(), "Strategy B": StrategyB(), "Strategy C": StrategyC()}


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        redirect(url_for("generate"))
    else:
        return render_template("home.html", strategies=strategies)


@app.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        form_size = request.form["size"]
        form_s = request.form["s"]
        form_n = request.form["n"]
        form_N = request.form["N"]
        form_strategy = request.form["strategy"]

        return redirect(url_for("result", strategy=form_strategy,
                                size=form_size, s=form_s, n=form_n, N=form_N))
    else:
        return render_template("generate.html", strategies=strategies)


@app.route("/result/<strategy>/<size>/<s>/<n>/<N>")
def result(strategy, size, s, n, N):

    mstrategy = strategies[strategy]
    mgenerator = Generator(mstrategy)
    mgenerator.s = int(s)
    mgenerator.n = int(n)
    mgenerator.N_connections = int(N)
    maze_result = mgenerator.generate(int(size))

    return render_template("result.html", result=maze_result)


if __name__ == "__main__":
    app.run(debug=True)
