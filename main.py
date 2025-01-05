from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        redirect(url_for("generate"))
    else:
        return render_template("home.html")


@app.route("/generate")
def generate():
    return render_template("generate.html")


if __name__ == "__main__":
    app.run(debug=True)
