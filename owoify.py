from flask import Flask, request
import hahalolcipher as hahalol

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/owoify", methods=['GET', 'POST'])
def owoify():
    text = request.values.get("text", "owo")
    return text.replace("l", "w").replace("r", "w").replace("L", "W").replace("R", "W")

@app.route("/hahalol", methods=['GET', 'POST'])
def enhahalol():
    text = request.values.get("text", "")
    if text:
        return hahalol.encrypt(text)
    return "Please provide text.", 400

@app.route("/dehahalol", methods=['GET', 'POST'])
def dehahalol():
    text = request.values.get("text", "")
    if text:
        try:
            return hahalol.decrypt(text)
        except:
            return "Invalid text.", 400
    return "Please provide text.", 400


if __name__ == "__main__":
    app.run()

