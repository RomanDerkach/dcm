"""application file."""
from flask import Flask, render_template
from connection import get_images
app = Flask(__name__, template_folder='templates/')


@app.route("/")
def hello():
    """That the first."""
    get_images()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
