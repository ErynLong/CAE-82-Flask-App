from app import app
from .forms import LoginForm, RegisterForm
from flask import render_template, request, flash, redirect, url_for
import requests
from .models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=='POST' and form.validate_on_submit():
        #We will do the login Stuff
        email = request.form.get('email').lower()   
        password = request.form.get('password')
        u = User.query.filter_by(email=email).first()
        if u and u.check_hashed_password(password):
            #good email and password
            login_user(u)
            flash('Welcome to Fakebook','success')
            return redirect(url_for('index')) #good login
        flash('Incorrect Email password Combo','danger')
        return render_template('login.html.j2',form=form) #bad login
    return render_template('login.html.j2',form=form) #get req

@app.route('/logout')
@login_required
def logout():
    if current_user:
        logout_user()
        flash('You have logged out', 'warning')
        return redirect(url_for('login'))


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method =='POST' and form.validate_on_submit():
        # Create a new user
        try:
            new_user_data = {
                "first_name":form.first_name.data.title(),
                "last_name":form.last_name.data.title(),
                "email":form.email.data.lower(),
                "password":form.password.data
            }
            #create an empty User
            new_user_object = User()
            #build user with form data
            new_user_object.from_dict(new_user_data)
            #save user to the database
            new_user_object.save()
        except:
            flash('There was an unexpected Error creating your Account Please Try Again.','danger')
            #Error Return
            return render_template('register.html.j2', form = form)
        # If it worked
        flash('You have registered successfully', 'success')
        return redirect(url_for('login'))
    #Get Return
    return render_template('register.html.j2', form = form)

@app.route('/students', methods=['GET'])
@login_required
def students():
    my_students = ['Caleb', 'Kristen', 'Eryn', 'Zak', 'David']
                                            #  Name in Jinja = name in python
    return render_template('students.html.j2', students = my_students)

@app.route('/ergast', methods = ['GET', 'POST'])
@login_required
def ergast():
    if request.method == 'POST':
        #contact the api and get the info for the year and round from the form
        year = request.form.get('year')
        round = request.form.get('round')
        url = f"http://ergast.com/api/f1/{year}/{round}/driverStandings.json"
        response = requests.get(url)
        if response.ok:
            data = response.json()["MRData"]["StandingsTable"]["StandingsLists"]
            if len(data)<=0:
                print('here')
                error_string = f"There is no info for {year} round {round}"
                return render_template('ergast.html.j2', error = error_string)
            
            all_racers=[]
            for racer in data[0].get("DriverStandings"):
                racer_dict={}
                racer_dict={
                    'first_name':racer['Driver']['givenName'],
                    'last_name':racer['Driver']['familyName'],
                    'position':racer['position'],
                    'wins':racer['wins'],
                    'DOB':racer['Driver']['dateOfBirth'],
                    'nationality':racer['Driver']['nationality'],
                    'constructor':racer['Constructors'][0]['name']
                }
                all_racers.append(racer_dict)
            return render_template('ergast.html.j2', racers = all_racers)
        else:
            error_string = "Houston We Have a Problem"
            return render_template('ergast.html.j2', error = error_string)
    return render_template('ergast.html.j2')