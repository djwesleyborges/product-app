from ninja import Schema, ModelSchema
from ninja.orm import create_schema

from product.models import Product, Color, Size

# SizeImageSchema = create_schema(Product, depth=1, fields=('size',))
ColorSchema = create_schema(Color, fields=('color',))
SizeSchema = create_schema(Size, depth=1, fields=('size',))


class ProductSchema(ModelSchema):

    class Config:
        model = Product
        model_fields = ('id', 'name', 'price', 'image', 'color', 'size')


class NotFoundSchema(Schema):
    message: str
