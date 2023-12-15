from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import Estoque, EstoqueEntrada, EstoqueSaida, EstoqueItens
from .schema import EstoqueSchema, EstoqueEntradaSchema, EstoqueSaidaSchema, EstoqueItensSchema

api = NinjaAPI()

@api.get('/estoque-entrada', response=List[EstoqueEntradaSchema])
def estoque_entrada(request):
    ...