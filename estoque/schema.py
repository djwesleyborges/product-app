from ninja import Schema, ModelSchema
from . import models


class EstoqueSchema(ModelSchema):
    class Meta:
        model = models.Estoque
        fields = "__all__"


class EstoqueEntradaSchema(ModelSchema):
    class Meta:
        model = models.EstoqueEntrada
        fields = "__all__"


class EstoqueSaidaSchema(ModelSchema):
    class Meta:
        model = models.EstoqueSaida
        fields = "__all__"


class EstoqueItensSchema(ModelSchema):
    class Meta:
        model = models.EstoqueItens
        fields = "__all__"
