from ninja import ModelSchema
from ninja.orm import create_schema

from . import models

EstoqueEntradaSchema = create_schema(models.EstoqueEntrada)
EstoqueSaidaSchema = create_schema(models.EstoqueSaida)


class EstoqueItemSchema(ModelSchema):
    class Config:
        model = models.EstoqueItem
        model_fields = ('produto', 'quantidade',)


class EstoqueSchema(ModelSchema):
    estoque_item: list[EstoqueItemSchema] = None

    class Config:
        model = models.Estoque
        model_fields = ('nf',)
