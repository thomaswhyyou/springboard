from sqlalchemy import Column, Integer, Text

from springboard.models import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text)

    def __repr__(self):
        return "<User {}: {}>".format(self.id, self.name)
