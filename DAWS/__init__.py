from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

class Upload_Image(FlaskForm):
    file = FileField("asdf")
    submit = SubmitField("Upload Files")

@app.route("/", methods=["GET", "POST"])
def index():
    form = Upload_Image()

    return render_template("index.html", form=form)
