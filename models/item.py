from models.db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)

    # one-to-many
    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=True
    )
    store = db.relationship("StoreModel", back_populates="items")

    # many-to-many
    tags = db.relationship("TagModel", back_populates="items", secondary="item_tag")
