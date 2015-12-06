from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, orm
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql.functions import now

from springboard.models import Base


class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"))
    pinned_product_refs = orm.relationship("BoardProductPinnedRef",
                                           cascade="all, delete-orphan",
                                           order_by="desc(BoardProductPinnedRef.pinned_at)")
    pinned_products = association_proxy("pinned_product_refs", "product",
                                        creator=lambda product: BoardProductPinnedRef(product=product))

    def __repr__(self):
        return "<Board {}: {}>".format(self.id, self.name)


class BoardProductPinnedRef(Base):
    __tablename__ = "board_product_pinned_refs"

    board_id = Column(Integer, ForeignKey("boards.id", ondelete="cascade"),
                      primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="cascade"),
                        primary_key=True)
    pinned_at = Column(DateTime, default=now())
    product = orm.relationship("Product")
