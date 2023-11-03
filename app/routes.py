from flask import render_template, redirect, url_for
from app import app
from app.forms import LoginForm, PlayerForm, CoachForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/coach', methods=['GET', 'POST'])
def coach():
    form = CoachForm()
    if form.validate_on_submit():
        # Process the form data (e.g., save it to a database)
        return redirect(url_for('coach'))  # Replace 'success' with your success page
    return render_template('coach.html', form=form)


@app.route('/player', methods=['GET', 'POST'])
def player():
    form = PlayerForm()
    if form.validate_on_submit():
        # Process the form data (e.g., save it to a database)
        return redirect(url_for('player'))  # Replace 'success' with your success page
    return render_template('player.html', form=form)
