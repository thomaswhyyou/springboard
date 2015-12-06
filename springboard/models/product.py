from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    Text,
    Boolean,
    DateTime,
    ForeignKey,
    orm,
)
from sqlalchemy.sql.functions import now

from springboard.models import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    original_price = Column(Numeric)
    price = Column(Numeric)
    is_on_sale = Column(Boolean)
    photo_url = Column(Text)
    created_at = Column(DateTime, default=now())

    # XXX: Just take them in as lowercase text value for simplicity.
    target_gender = Column(Text)

    # XXX: Ignore taxonomy hierarchy and track only the top most level
    # as 'category' in products table for the sake of simplicity.
    category = Column(Text)

    vendor_id = Column(Integer, ForeignKey("vendors.id", ondelete="cascade"))
    vendor = orm.relationship("Vendor", backref="products")

    def __repr__(self):
        return "<Product {}: {}>".format(self.id, self.name)
