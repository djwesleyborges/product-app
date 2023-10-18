from ninja import Schema


class ProductSchema(Schema):
    name: str
    price: str
    color: str
    size: str


class NotFoundSchema(Schema):
    message: str
