from app import db, login
from flask_login import UserMixin # This is just for the User model!
from datetime import datetime as dt, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

followers = db.Table(
    'followers',
    db.Column('follower_id',db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id',db.Integer, db.ForeignKey('user.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), index=True, unique=True)
    password = db.Column(db.String(200))
    # icon = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default = dt.utcnow)
    gratitudeposts = db.relationship('GratitudePost', backref='author', lazy="dynamic")
    lyricsposts = db.relationship('LyricsPost', backref='author', lazy="dynamic")
    promptsposts = db.relationship('PromptsPost', backref='author', lazy="dynamic")
    followed = db.relationship(
        'User',
        secondary = followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers',lazy='dynamic'),
        lazy='dynamic'
    )
    token = db.Column(db.String, index=True, unique=True)
    token_exp = db.Column(db.DateTime)
    is_admin = db.Column(db.Boolean, default=False)
    

    ##################################################
    ############## Methods for Token auth ############
    ##################################################

    def get_token(self, exp=86400):
        current_time = dt.utcnow()
        #give the user their token if it is not expired
        if self.token and self.token_exp > current_time + timedelta(seconds=60):
            return self.token
        #if the token DNE or token is exp
        self.token = secrets.token_urlsafe(32)
        self.token_exp = current_time + timedelta(seconds=exp)
        self.save()
        return self.token

    def revoke_token(self):
        self.token_exp = dt.utcnow() - timedelta(seconds=61)

    @staticmethod
    def check_token(token):
        u = User.query.filter_by(token=token).first()
        if not u or u.token_exp < dt.utcnow():
            return None
        return u
    #########################################
    ############# End Methods for tokens ####
    #########################################

    def __repr__(self):
        return f'<User: {self.id} | {self.email}>'
    
    # wE WANT TO BE ABLE TO CHECK IF THE USER IS FOLLOWING SOMEONE
    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    #follow a user
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            db.session.commit()
    
    # unfollow a user
    def unfollow(self,user):
        if self.is_following(user):
            self.followed.remove(user)
            db.session.commit()
    
    # get all the post from the user I am following
    def gratitude_followed_posts(self):
        #get posts for all the users I'm following
        followed = GratitudePost.query.join(followers,(GratitudePost.user_id == followers.c.followed_id)).filter(followers.c.follower_id == self.id)
        #get all my own posts
        self_posts = GratitudePost.query.filter_by(user_id=self.id)
        #add those together and then I will sort then my dates in descending order
        all_posts = followed.union(self_posts).order_by(GratitudePost.date_created.desc())
        return all_posts
    
    def lyrics_followed_posts(self):
        #get posts for all the users I'm following
        followed = LyricsPost.query.join(followers,(LyricsPost.user_id == followers.c.followed_id)).filter(followers.c.follower_id == self.id)
        #get all my own posts
        self_posts = LyricsPost.query.filter_by(user_id=self.id)
        #add those together and then I will sort then my dates in descending order
        all_posts = followed.union(self_posts).order_by(LyricsPost.date_created.desc())
        return all_posts
    
    def prompts_followed_posts(self):
        #get posts for all the users I'm following
        followed = PromptsPost.query.join(followers,(PromptsPost.user_id == followers.c.followed_id)).filter(followers.c.follower_id == self.id)
        #get all my own posts
        self_posts = PromptsPost.query.filter_by(user_id=self.id)
        #add those together and then I will sort then my dates in descending order
        all_posts = followed.union(self_posts).order_by(PromptsPost.date_created.desc())
        return all_posts

    #salts and hashes our password to make it hard to steal
    def hash_password(self, original_password):
        return generate_password_hash(original_password)
    
    # compares the user password to the password provided in the login form
    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])
        # self.icon = data['icon']


    ### NEW
    def to_dict(self):
        return {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email,
            # "icon":self.icon,
            "created_on":self.created_on,
            "is_admin":self.is_admin,
            "token":self.token
        }

    # saves the user to the database
    def save(self):
        db.session.add(self) # add the user to the db session
        db.session.commit() #save everything in the session to the database

    # def get_icon_url(self):
    #     return f'https://avatars.dicebear.com/api/big-smile/{self.icon}.svg'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    # SELECT * FROM user WHERE id = ???

class LyricsPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.id} | {self.body[:15]}>'


    def to_dict(self):
        return {
            'id':self.id,
            'body':self.body,
            'date_created':self.date_created,
            'date_updated':self.date_updated,
            'user_id':self.user_id
        }

    def edit(self, new_body):
        self.body = new_body
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # saves the post to the database
    def save(self):
        db.session.add(self) # add the user to the db session
        db.session.commit() #save everything in the session to the database

class GratitudePost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.id} | {self.body[:15]}>'


    def to_dict(self):
        return {
            'id':self.id,
            'body':self.body,
            'date_created':self.date_created,
            'date_updated':self.date_updated,
            'user_id':self.user_id
        }

    def edit(self, new_body):
        self.body = new_body
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # saves the post to the database
    def save(self):
        db.session.add(self) # add the user to the db session
        db.session.commit() #save everything in the session to the database

class PromptsPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.id} | {self.body[:15]}>'


    def to_dict(self):
        return {
            'id':self.id,
            'body':self.body,
            'date_created':self.date_created,
            'date_updated':self.date_updated,
            'user_id':self.user_id
        }

    def edit(self, new_body):
        self.body = new_body
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # saves the post to the database
    def save(self):
        db.session.add(self) # add the user to the db session
        db.session.commit() #save everything in the session to the database