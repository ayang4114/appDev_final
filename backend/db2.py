from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def  __init__(self, **kwargs):
        self.code = kwargs.get('code', '')
        self.name = kwargs.get('name', '')
        self.user_id = kwargs.get('user_id', '')
    
    def serialize(self):
        return{
            'name': self.name,
            'code': self.code
        }


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    netid = db.Column(db.String, nullable=False)
    favo_location = db.relationship('Location')
    classes = db.relationship("Class", cascade='delete')

    def __init__ (self, **kwargs):
        self.name = kwargs.get('name', '')
        self.netid= kwargs.get('netid', '')

    def serialize(self):
        return{
            'name': self.name,
            'netid': self.netid,
            'classes': [c.serialize() for c in self.classes]
        }

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    def __init__ (self, **kwargs):
        self.name = kwargs.get('name')
        self.user_id = kwargs.get('user_id')
    
    def serialize(self):
        return{
            'location_name': self.name
        }

class Chats(db.Model):
    __tablename__ = "chats"
    id = db.Column(db.Integer, primary_key=True)
    chat_name = db.Column(db.String, nullable=False)
    posts = db.relationship('Posts', cascade='delete')
 
    def __init__ (self, **kwargs):
        self.chat_name = kwargs.get('chat_name', '')

    def serialize(self):
        return{
            'chatname': self.chat_name,
            'post': [post.serialize() for post in self.posts]
        }

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    user_netid = db.Column(db.String, nullable=False)
    chatname = db.Column(db.String, nullable=False)
    chat_id = db.Column(db.String, db.ForeignKey('chats.id'), nullable=False)

    def __init__ (self, **kwargs):
        self.username = kwargs.get('username')
        self.text = kwargs.get('text')
        self.user_netid = kwargs.get('user_netid')
        self.chatname = kwargs.get('chatname')
        self.chat_id = kwargs.get('chat_id')
    
    def serialize(self):
        return{
            'text': self.text,
            'username': self.username,
            'chatname': self.chatname
        }



