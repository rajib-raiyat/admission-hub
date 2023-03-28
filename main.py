from flask import Flask, render_template

app = Flask(__name__, template_folder='front-end/templates', static_folder='front-end/assets')


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/university-list")
def university():
    return render_template('University.html')


@app.route("/confirm-form")
def confirm_form():
    return render_template('Form.html')


@app.route("/std-login")
def std_login():
    return render_template('LoginStu.html')


@app.route("/uni-login")
def uni_login():
    return render_template('LoginUni.html')
