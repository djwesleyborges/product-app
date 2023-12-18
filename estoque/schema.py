from ninja import ModelSchema
from product.models import Product
from ninja.orm import create_schema

from . import models

EstoqueSchema = create_schema(models.Estoque)
EstoqueEntradaSchema = create_schema(models.EstoqueEntrada)
EstoqueSaidaSchema =  create_schema(models.EstoqueSaida)


# class EstoqueSchema(ModelSchema):
#     class Config:
#         model = models.Estoque
#         model_fields = '__all__'


# class EstoqueEntradaSchema(ModelSchema):
#     product = list[Product]
#
#     class Config:
#         model = models.EstoqueEntrada
#         model_fields = '__all__'

# class EstoqueSaidaSchema(ModelSchema):
#     class Config:
#         model = models.EstoqueSaida
#         model_fields = '__all__'
#
#
# class EstoqueItensSchema(ModelSchema):
#     class Config:
#         model = models.EstoqueItens
#         model_fields = '__all__'
