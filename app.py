from flask import Flask,render_template
import flask as f
import gunicorn
app = Flask(__name__)

@app.route('/')
def home1():
    return render_template("index.html")
@app.route('/greet')
def home():
    return "Hello"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

