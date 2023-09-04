from marshmallow import Schema, fields
from schema import BaseStoreSchema, BaseTagSchema


class BaseItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class ItemSchema(BaseItemSchema):
    store_id = fields.Str(required=True)
    store = fields.Nested(BaseStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(BaseTagSchema()), dump_only=True)
