from ninja import Schema, ModelSchema
from product.models import Product, Color, Size, Image


class ColorSchema(ModelSchema):
    class Config:
        model = Color
        model_fields = ('color',)


class SizeSchema(ModelSchema):
    class Config:
        model = Size
        model_fields = ('size',)


class ImageSchema(ModelSchema):
    class Config:
        model = Image
        model_fields = ('size', 'product', 'image', 'color')


class ProductSchema(ModelSchema):
    colors: list[ColorSchema] = None
    size: list[SizeSchema] = None
    image: list[ImageSchema] = None

    class Config:
        model = Product
        model_fields = ('id', 'name', 'price',)


class NotFoundSchema(Schema):
    message: str
