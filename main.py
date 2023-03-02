from flask import Flask, render_template

app = Flask(__name__, template_folder='front-end/templates', static_folder='front-end/assets')


@app.route("/")
def hello_world():
    return render_template('index.html')
