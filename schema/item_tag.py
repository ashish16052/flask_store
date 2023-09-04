from marshmallow import Schema, fields
from schema import ItemSchema, TagSchema


class ItemTagSchema(Schema):
    item = fields.Nested(ItemSchema())
    tag = fields.Nested(TagSchema())
