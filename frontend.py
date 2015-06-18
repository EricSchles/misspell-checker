from flask import Flask
from flask import request
from flask import render_template
from backend import MissSpell
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def my_form():
    text = request.form['text']
    level = request.form['level']
    percentage = int(request.form['percentage'])
    ms = MissSpell(level,percentage)
    processed_text = ms.checker(text)
    return processed_text

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
        )
