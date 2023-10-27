from ninja import Schema, ModelSchema
from product.models import Product, Color, Size


class ColorSchema(ModelSchema):
    class Config:
        model = Color
        model_fields = ('color',)


class SizeSchema(ModelSchema):
    class Config:
        model = Size
        model_fields = ('size',)


class ProductSchema(ModelSchema):
    colors: list[ColorSchema] = None
    size: list[SizeSchema] = None

    class Config:
        model = Product
        model_fields = ('id', 'name', 'price', 'image')


class NotFoundSchema(Schema):
    message: str
