from flask import Flask
import flask as f
import gunicorn
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"
print(f.__version__)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

