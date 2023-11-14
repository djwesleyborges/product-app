from ninja import Schema, ModelSchema
from ninja.orm import create_schema

from product.models import Product, Color, Size, Image


class SizeSchema(ModelSchema):
    class Config:
        model = Size
        model_fields = ('size',)


ColorSchema = create_schema(Color, fields=('color',))

# class ColorSchema(ModelSchema):
#     size: list[SizeSchema] = None

#     class Config:
#         model = Color
#         model_fields = ('color',)


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
