# app.py

from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_s3 import FlaskS3
import boto3
app = Flask(__name__)
# app.config['MULTIPLE-SCREENS'] = 'multiple-screens'
s3 = bot3.resource('s3')
bucket = s3.Bucket('multiple-screens')

# This line is required for the flask configuration in order to pass variables
app.config['SECRET_KEY'] = 'you-will-never-guess'


# Create class that will hold the form information
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Redirect root to the index_post function which displays the form
@app.route('/')
def index():
    return redirect(url_for('index_post'))


# main function, methods must be set in order to take information from form
@app.route('/index', methods=['GET', 'POST'])
def index_post():
    # Create instance of the form
    form = LoginForm()  # type: LoginForm
    # Check if submit button has been pressed
    if request.method == 'POST':
        # Extract name from form and save in variable name
        name = form.username.data
        # Loads next page and gives it the name variable
        return redirect(url_for('name', name=name))
    # If submit button not pressed display index page with the form
    return render_template('index.html', title='Sign In', form=form)


# Name page must have the /<name> for the variable to be used
@app.route('/name/<name>', methods=['GET', 'POST'])
def name(name):
    return render_template('name.html', name=name)


# This is to run the app locally for testing
if __name__ == '__main__':
    app.run(debug=True)




class FlaskS3(app=app):
    init_app(app)
    flask_s3.create_all(app=app, bucket_name=multiple-screens)
