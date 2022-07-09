from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from password_generator import passgen

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"


# Forms
class PasswordForm(FlaskForm):
    password_length = IntegerField(label="Password Length", validators=[DataRequired(), NumberRange(12, 64)])
    submit = SubmitField(label="Generate")


# Routes
@app.route('/', methods=["GET", "POST"])
def index():
    title = "Password Generator"
    form = PasswordForm()
    if form.validate_on_submit():
        mypassword = passgen(form.password_length.data)
        return render_template("index.html", mypassword=mypassword, form=form, title=title)
    return render_template("index.html", form=form, title=title)


if __name__ == '__main__':
    app.run(debug=True)
