from sqlalchemy import Column, String, Integer
from app import db

class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    def __iter__(self):
        yield 'id', self.id
        yield 'title', self.title
        yield 'content', self.content

