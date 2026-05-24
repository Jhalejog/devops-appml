from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/services")
def services():
    return "version 1 work in progress"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080)

