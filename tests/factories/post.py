import factory
import logging
from faker import Faker
from app import db
from app.models import Post

faker = Faker('pt_BR')

class PostFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Post
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    title = factory.LazyAttribute(lambda x: faker.name())
    content = factory.LazyAttribute(lambda x: faker.sentence(nb_words=50))
