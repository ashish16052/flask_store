from flask.views import MethodView
from flask_smorest import Blueprint
from models import ItemModel, TagModel
from models.db import db
from schema import ItemSchema,ItemTagSchema, TagSchema

blueprint = Blueprint("items", __name__)


@blueprint.route("/item")
class ItemList(MethodView):
    @blueprint.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @blueprint.arguments(ItemSchema)
    @blueprint.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(
            name=item_data['name'],
            price=item_data['price'],
            store_id=item_data['store_id'],
        )
        db.session.add(item)
        db.session.commit()
        return item


@blueprint.route("/item/<string:item_id>")
class Item(MethodView):
    @blueprint.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.filter_by(id=item_id).first()
        return item

    @blueprint.arguments(ItemSchema)
    @blueprint.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.filter_by(id=item_id).first()
        item.name = item_data['name']
        item.price = item_data['price']
        db.session.add(item)
        db.session.commit()
        return item

    def delete(self, item_id):
        item = ItemModel.query.filter_by(id=item_id).first()
        db.session.delete(item)
        db.session.commit()
        return {'message': 'item deleted'}, 200


@blueprint.route("/item/<string:item_id>/tag/<string:tag_id>")
class ItemTag(MethodView):
    @blueprint.response(200, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.filter_by(id=item_id).first()
        tag = TagModel.query.filter_by(id=tag_id).first()

        item.tags.append(tag)

        db.session.add(item)
        db.session.commit()
        return tag
                

    @blueprint.response(200, ItemTagSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.filter_by(id=item_id).first()
        tag = TagModel.query.filter_by(id=tag_id).first()

        item.tags.remove(tag)

        db.session.add(item)
        db.session.commit()
        return {"item":item, "tag":tag}
