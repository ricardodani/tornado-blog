# -*- coding: utf-8 -*-

import datetime
import markdown
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(255))
    comments = sa.orm.relationship('Comment', backref='user')
    posts = sa.orm.relationship('Post', backref='author')
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<User(id='{}', username='{}')>".format(self.id, self.username)


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(255))
    description = sa.Column(sa.String(255))
    text = sa.Column(sa.Text)
    comments = sa.orm.relationship('Comment', backref='post')
    author_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Post(id='{}', title='{}')>".format(self.id, self.title)

    @property
    def html(self):
        return markdown.markdown(self.text)

    @classmethod
    def get_recent_posts(cls, db):
        return db.query(cls).order_by(sa.desc(cls.created_at)).all()[:5]

    @classmethod
    def get_posts(cls, db):
        return db.query(cls).all()


class Comment(Base):
    __tablename__ = 'comments'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    post_id = sa.Column(sa.Integer, sa.ForeignKey('posts.id'))
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Comment(id='{}', user_id='{}', post_id='{}')>".format(
            self.id, self.user_id, self.post_id
        )
