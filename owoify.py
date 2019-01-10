from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/owoify", methods=['GET', 'POST'])
def owoify():
	text = request.values.get("text", "owo")
	return text.replace("l", "w").replace("r", "w").replace("L", "W").replace("R", "W")

if __name__ == "__main__":
    app.run()

