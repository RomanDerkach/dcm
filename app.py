"""application file."""
from flask import Flask, render_template
app = Flask(__name__, template_folder='/home/roman/Desktop/web/dcm/templates')


@app.route("/")
def hello():
    """That the first."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
