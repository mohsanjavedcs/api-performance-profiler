from flask import Flask # type: ignore
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>API Endpoint is working.</h1>"

@app.route("/fast")
def fast():
    return "<h1>The fast endpoint is working.</h1>"

@app.route("/delayed")
def delayed():
    time.sleep(0.2)
    return "<h1>The delayed endpoint is working.</h1>"

if __name__ == "__main__":
    app.run(debug=True)