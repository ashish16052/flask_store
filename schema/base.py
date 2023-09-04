from marshmallow import Schema, fields


class BaseItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class BaseStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class BaseTagSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)