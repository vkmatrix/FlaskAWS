from flask import Flask
import flask as f
import gunicorn
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

