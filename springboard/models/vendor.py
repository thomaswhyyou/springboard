from sqlalchemy import Column, Integer, Text

from springboard.models import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)
    name = Column(Text)

    def __repr__(self):
        return "<Vendor {}: {}>".format(self.id, self.name)
