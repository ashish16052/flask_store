from models.db import db


class ItemTagModel(db.Model):
    __tablename__ = "item_tag"

    id = db.Column(db.Integer, primary_key=True)

    # many-to-many relationship
    item_id = db.Column(
        db.Integer, db.ForeignKey("items.id")
    )
    tag_id = db.Column(
        db.Integer, db.ForeignKey("tags.id")
    )
