import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'

    id = Column(Integer, primary_key=True, autoincrement=True) 
    user_from_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('User.id'), nullable=False)

    # Relacionar con la tabla User
    user_from = relationship('User', foreign_keys=[user_from_id], backref='following')
    user_to = relationship('User', foreign_keys=[user_to_id], backref='followers')

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), primary_key=True)



class Comment(Base):
    __tablename__ = 'Comment'
    # Definir columnas para la tabla Comment
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

    # Relación entre Comment y User
    author = relationship('User', backref='comments')

    # Relacion entre Comment y Post
    post = relationship('Post', backref= 'comments')

class Post (Base):
    __tablename__= 'Post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)

    # Relacion entre Comment y User
    user = relationship('User', backref="post")

class Media (Base): 
    __tablename__ = 'Media'

    id = Column(Integer, primary_key=True)
    type =Column(String)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

    # Relacion entre Media y Post
    post = relationship('Post', backref='posts')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
