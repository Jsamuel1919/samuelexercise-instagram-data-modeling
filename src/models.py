import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):

    __tablename__ ='users'
    id = Column(Integer, primary_key= True)
    username = Column(String(250))
    email = Column(String(200))
    profile_picture = Column(String(250))
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    image_url = Column(String(250))
    caption = Column(String(250))
    user = relationship("User", back_populates="posts")

class Comment(Base):

    __tablename__ = 'comments'
    id = Column(Integer, primary_key = True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String(250))

class Like(Base):

    __tablename__ = 'likes'
    id = Column(Integer, primary_key = True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
