from crypt import methods
from enum import unique
from wsgiref.validate import validator
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,SubmitField
from wtforms.validators import  InputRequired,Length, ValidationError
from flask_bcrypt import Bcrypt



#initializing the app
app = Flask(__name__)

#initioalizing the db and conncetion string
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #using sqlite3
app.config['SECRET_KEY'] = 'nkemakolam' #for securing our session cookies
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://nkemakolam:ghosts123@localhost/bitcoindb'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
#login mapper

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    

#creating the  User database through class
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False,unique=True)
    password = db.Column(db.String(255), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(min=4,max=20)],
    render_kw = {"placeholder":"Username"})
    password = StringField(validators=[InputRequired(),Length(min=4,max=20)],
    render_kw = {"placeholder":"Password"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()

        if existing_user_username:
            raise ValidationError(
                "That user name exist in the database please use a different one"
            )


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(min=4,max=20)],
    render_kw = {"placeholder":"Username"})
    password = PasswordField(validators=[InputRequired(),Length(min=4,max=20)],
    render_kw = {"placeholder":"Password"})

    submit = SubmitField("Login")
   





@app.route('/')
def method_name():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user:
            password = bcrypt.check_password_hash(user.password,form.password.data)
            print(password)
            if password == True:
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html',form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        pw_hash = bcrypt.generate_password_hash(hashed_password).decode('utf-8')
        new_user = User(username=form.username.data, password=pw_hash)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',form=form)



if __name__ == '__main__':
     app.run(debug=True)