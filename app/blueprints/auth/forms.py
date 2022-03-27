# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.models import User
# import random
from jinja2 import Markup

class LoginForm(FlaskForm):
    #field name = DatatypeField('LABEL', validators=[LIST OF validators])
    email = StringField('Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name= StringField('First Name',validators=[DataRequired()])
    last_name= StringField('Last Name',validators=[DataRequired()])
    email = StringField('Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('password',
            message='Passwords must match')])
    submit = SubmitField('Register')
    
# https://avatars.dicebear.com/api/big-smile/123.svg
    # r1=random.randint(1,1000)
    # r2=random.randint(1001,2000)
    # r3=random.randint(2001,3000)
    # r4=random.randint(3001,4000)

    # r1_img=Markup(f'<img src="https://avatars.dicebear.com/api/big-smile/{r1}.svg" style="height:75px">')
    # r2_img=Markup(f'<img src="https://avatars.dicebear.com/api/big-smile/{r2}.svg" style="height:75px">')
    # r3_img=Markup(f'<img src="https://avatars.dicebear.com/api/big-smile/{r3}.svg" style="height:75px">')
    # r4_img=Markup(f'<img src="https://avatars.dicebear.com/api/big-smile/{r4}.svg" style="height:75px">')

    # icon = RadioField('Avatar', validators=[DataRequired()],
    #         choices=[(r1, r1_img),(r2, r2_img),(r3,r3_img),(r4, r4_img)])
            

    # MUST BE LIKE THIS VALIDATE_FIELDNAME
    def validate_email(form, field):
                                                            #give me only the first result returns 1 user object
        same_email_user = User.query.filter_by(email = field.data).first()
                        # SELECT * FROM user WHERE email = ???
                        # filter_by always gives a list (unless you use first())
        if same_email_user:
            raise ValidationError('Email is Already in Use')

class EditProfileForm(FlaskForm):
    first_name= StringField('First Name',validators=[DataRequired()])
    last_name= StringField('Last Name',validators=[DataRequired()])
    email = StringField('Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('password',
            message='Passwords must match')])
    submit = SubmitField('Update')
    
    # r1=random.randint(1,1000)
    # r2=random.randint(1001,2000)
    # r3=random.randint(2001,3000)
    # r4=random.randint(3001,4000)

    # r1_img=Markup(f'<img src="https://avatars.dicebear.com/api/big-smile/{r1}.svg" style="height:75px">')
    # r2_img=Markup(f'<img src="https://avatars.dicebear.com/api/big-smile/{r2}.svg" style="height:75px">')
    # r3_img=Markup(f'<img src="https://avatars.dicebear.com/api/big-smile/{r3}.svg" style="height:75px">')
    # r4_img=Markup(f'<img src="https://avatars.dicebear.com/api/big-smile/{r4}.svg" style="height:75px">')

    # icon = RadioField('Avatar', validators=[DataRequired()],
    #         choices=[(9000,"Don't Change"),(r1, r1_img),(r2, r2_img),(r3,r3_img),(r4, r4_img)])
            
