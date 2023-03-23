from app import app, db
from flask import render_template, redirect, url_for, flash
# from fake_data import posts
from app.forms import SignUpForm
from app.models import User

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Form page

@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Create an instance of the form (in the context of the current request)
    form = SignUpForm()
    # Check if the form was submitted and that all of the fields are valid
    if form.validate_on_submit():
        # If so, get the data from the form fields
        print('Hooray our form was validated!!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phoneno = form.phoneno.data
        address = form.address.data
        # maybe they need to submit it or something
        print(first_name, last_name, phoneno, address)
        # I think this will make it work for what's wanted but
        # I need to keep looking at it
        new_user = User(first_name=first_name, last_name=last_name, phoneno=phoneno, address=address)
        flash(f"Thank you {first_name} for signing up!", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)
