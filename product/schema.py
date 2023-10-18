from ninja import Schema
from product.models import Product, Color, Size


class ColorSchema(Schema):
    color: str


class SizeSchema(Schema):
    size: str


class ProductSchema(Schema):
    name: str
    price: int
    colors: ColorSchema
    size: SizeSchema
    # class Config:
    #     model = Product
    #     model_fields = ['name', 'price', 'colors', 'size']


class NotFoundSchema(Schema):
    message: str
