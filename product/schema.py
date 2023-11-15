from ninja import Schema, ModelSchema
from ninja.orm import create_schema

from product.models import Product, Color, Size, Image


ColorSchema = create_schema(Color, fields=('color',))

SizeImageSchema = create_schema(Image, depth=1, fields=('size',))


class ImageSchema(ModelSchema):
    class Config:
        model = Image
        model_fields = ('product', 'image', 'color')


class ProductSchema(ModelSchema):
    colors: list[ColorSchema] = None
    image: list[ImageSchema] = None

    class Config:
        model = Product
        model_fields = ('id', 'name', 'price',)


class NotFoundSchema(Schema):
    message: str
