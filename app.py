from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    return render_template()

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="10.0.0.136", port=5000)
