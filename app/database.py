from flask_pymongo import PyMongo

from app import app

app.config['MONGO_DBNAME'] = 'users'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users'

mongo = PyMongo(app)

# Model = declarative_base(name='Model')

class User():#Model):
    # __tablename__ = 'users'
    # id = Column('user_id', Integer, primary_key=True)
    # openid = Column('openid', String(200))
    # name = Column(String(200))

    def __init__(self, name, openid):
        self.name = name
        self.openid = openid

    # def to_json(self):
    #     return dict(name=self.name, is_admin=self.is_admin)

    # @property
    # def is_admin(self):
    #     return self.openid in app.config['ADMINS']

    # def __eq__(self, other):
    #     return type(self) is type(other) and self.id == other.id

    # def __ne__(self, other):
    #     return not self.__eq__(other)
