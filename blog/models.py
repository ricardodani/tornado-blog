import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    text = sa.Column(sa.Text)

    def __repr__(self):
        return "<Post(id='{}', title='{}')>".format(self.id, self.title)
