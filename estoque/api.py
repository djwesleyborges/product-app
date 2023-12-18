from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from product.models import Product
from .models import Estoque, EstoqueEntrada, EstoqueSaida
from .schema import EstoqueSchema, EstoqueEntradaSchema#, EstoqueSaidaSchema, EstoqueItensSchema

api = NinjaAPI()


@api.get('/estoque-entrada')
def estoque_entrada(request, nf: int, qtd: int, product_id: int):
    product = Product.objects.get(product_id)
    estoque_entrada = EstoqueEntrada.objects.create()
    ...
