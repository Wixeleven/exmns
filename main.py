from flask import Flask, render_template, request
import wolframalpha

app = Flask(__name__)
client = wolframalpha.Client("P76EK3-XY6TKV2XYW")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    topic = request.form["topic"]
    query = topic
    res = client.query(query)
    result = ""
    for pod in res.pods:
        for sub in pod.subpods:
            result += sub.plaintext + "\n\n"
    return render_template("result.html", topic=topic, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
