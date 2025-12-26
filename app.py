from flask import Flask, render_template

app = Flask(__name__)

STREAMS = [f"drone{i}" for i in range(1, 11)]

@app.route("/")
def dashboard():
    return render_template("dashboard.html", streams=STREAMS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
