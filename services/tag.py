from flask.views import MethodView
from flask_smorest import Blueprint
from models import TagModel
from models.db import db
from schema import TagSchema

blueprint = Blueprint("tags", __name__)

@blueprint.route("/tag")
class TagList(MethodView):
    @blueprint.response(200, TagSchema(many=True))
    def get(self):
        return TagModel.query.all()


@blueprint.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blueprint.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.filter_by(id=tag_id).first()
        return tag

    @blueprint.arguments(TagSchema)
    @blueprint.response(200, TagSchema)
    def put(self, tag_data, tag_id):
        tag = TagModel.query.filter_by(id=tag_id).first()
        tag.name = tag_data['name']
        db.session.add(tag)
        db.session.commit()
        return tag

    def delete(self, tag_id):
        tag = TagModel.query.filter_by(id=tag_id).first()
        db.session.delete(tag)
        db.session.commit()
        return {'message': 'tag deleted'}, 200
