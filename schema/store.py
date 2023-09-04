from marshmallow import Schema, fields
from schema import BaseItemSchema, BaseTagSchema


class BaseStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class StoreSchema(BaseStoreSchema):
    items = fields.List(fields.Nested(BaseItemSchema(), dump_only=True))
    tags = fields.List(fields.Nested(BaseTagSchema(), dump_only=True))
