from flask.views import MethodView
from flask_smorest import Blueprint
from models import StoreModel, TagModel
from models.db import db
from schema import StoreSchema, TagSchema

blueprint = Blueprint("stores", __name__)


@blueprint.route("/store")
class StoreList(MethodView):
    @blueprint.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blueprint.arguments(StoreSchema)
    @blueprint.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(
            name=store_data['name'],
        )
        db.session.add(store)
        db.session.commit()
        return store


@blueprint.route("/store/<string:store_id>")
class Store(MethodView):
    @blueprint.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.filter_by(id=store_id).first()
        return store

    @blueprint.arguments(StoreSchema)
    @blueprint.response(200, StoreSchema)
    def put(self, store_data, store_id):
        store = StoreModel.query.filter_by(id=store_id).first()
        store.name = store_data['name']
        db.session.commit()
        return store

    def delete(self, store_id):
        store = StoreModel.query.filter_by(id=store_id).first()
        db.session.delete(store)
        db.session.commit()
        return {'message': 'store deleted'}, 200


@blueprint.route("/store/<string:store_id>/tag")
class StoreTag(MethodView):
    @blueprint.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.filter_by(id=store_id).first()
        return store.tags

    @blueprint.arguments(TagSchema)
    @blueprint.response(201, TagSchema)
    def post(self, tag_data, store_id):
        tag = TagModel(
            name=tag_data['name'],
            store_id=store_id,
        )
        db.session.add(tag)
        db.session.commit()
        return tag