from marshmallow import Schema, fields
from schema import BaseStoreSchema, BaseItemSchema


class BaseTagSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class TagSchema(BaseTagSchema):
    store_id = fields.Str()
    store = fields.Nested(BaseStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(BaseItemSchema()), dump_only=True)
