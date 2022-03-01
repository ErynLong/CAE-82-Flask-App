from app import db
from datetime import datetime as dt
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, index=True, unique=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    bio = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    modified_on = db.Column(db.DateTime, onupdate=dt.utcnow)
    videos = db.relationship("Video", backref="creator", lazy="dynamic", cascade='all, delete-orphan')
    votes = db.relationship("Vote", backref="voter", lazy="dynamic", cascade='all, delete-orphan')
    video_voted_on = db.relationship("Video", backref="voter", secondary="vote",  lazy="dynamic", viewonly=True)
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<{self.id}|{self.email}>'

class Vote(db.Model):
    vote_id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer,db.ForeignKey('video.video_id'))
    user_id = db.Column(db.Integer,db.ForeignKey('person.id'))
    vote = db.Column(db.Boolean())
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    modified_on = db.Column(db.DateTime, onupdate=dt.utcnow)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<{self.vote_id}|{self.vote}>'

    def from_dict(self,data):
        self.video_id = data['video_id']
        self.user_id = data['user_id']
        self.vote = data['vote']

    def to_dict(self):
        return {
            "vote_id": self.vote_id,
            "video_id": self.video_id,
            "user_id":self.user_id,
            "vote":self.vote,
            "created_on":self.created_on,
            "modified_on":self.modified_on,
            }

class Video(db.Model):
    video_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    cloud_id = db.Column(db.String)
    thumbnail_url = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    modified_on = db.Column(db.DateTime, onupdate=dt.utcnow)
    user_id = db.Column(db.ForeignKey('person.id'))
    votes = db.relationship("Vote", backref="vid", lazy="dynamic", cascade='all, delete-orphan')

    @property
    def up_votes(self):
        return Vote.query.filter(Vote.video_id==self.video_id, Vote.vote==True).count()

    @property
    def down_votes(self):
        return Vote.query.filter(Vote.video_id==self.video_id, Vote.vote==False).count()
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<{self.video_id}|{self.title}>'

    def from_dict(self,data):
        self.title = data['title']
        self.user_id = data['user_id']
        self.cloud_id=data['cloud_id']
        self.thumbnail_url=data['thumbnail_url']

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "title": self.title,
            "video_id":self.video_id,
            "created_on":self.created_on,
            "modified_on":self.modified_on,
            'cloud_id':self.cloud_id,
            "thumbnail_url":self.thumbnail_url,
            'up_votes':self.up_votes,
            'down_votes':self.down_votes,
            'creator_name':self.creator.name,
            'creator_id':self.creator.user_id,
            'creator_email':self.creator.email,
            "creator_bio":self.creator.bio,
            "creator_img":self.creator.img
            }
