from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from estoque.models import EstoqueEntrada, EstoqueSaida
from estoque.schema import EstoqueEntradaSchema, EstoqueSaidaSchema
from product.models import Product, Color, Size
from product.schema import (
    ProductSchema, NotFoundSchema, ColorSchema, SizeSchema
)

api = NinjaAPI()


@api.get('/product/colors/', response=List[ColorSchema])
def colors(request):
    return Color.objects.all()


@api.get('/product/{color}/sizes/', response=List[SizeSchema])
def get_sizes(request, color: str):
    color = get_object_or_404(Color, color=color)
    sizes = Size.objects.filter(product__color=color).distinct()
    return sizes


@api.get('/product/{color}/{size}/image/', response=ProductSchema)
def get_product_by_color_size(request, color: str, size: str):
    color = get_object_or_404(Color, color=color)
    size = get_object_or_404(Size, size=size)
    return Product.objects.filter(color=color, size=size).first()


@api.get('/product', response=List[ProductSchema])
def products(request, size: Optional[str] = None):
    if size:
        return Product.objects.filter(image__image__name=size)
    return Product.objects.all()


@api.get('/product/{product_id}', response={200: ProductSchema, 404: NotFoundSchema})
def product(request, product_id: str):
    product = get_object_or_404(Product, id=product_id)
    return product


@api.get('/products/{color}/{size}/', response=List[ProductSchema])
def get_similar_products(request, color: str, size: str):
    color = get_object_or_404(Color, color=color)
    size = get_object_or_404(Size, size=size)
    return Product.objects.filter(color=color, size=size)


@api.post('/estoque-entrada/', response=EstoqueEntradaSchema)
def estoque_entrada(request, nf: int, qtd: int, product_id: int):
    product = Product.objects.filter(pk=product_id)
    if product:
        estoque_entrada = EstoqueEntrada.objects.create(nf=nf, movimento='e', produto_id=product_id, quantidade=qtd)
        qtd_atual = Product.objects.get(pk=product_id).estoque
        Product.objects.filter(pk=product_id).update(estoque=qtd_atual + estoque_entrada.quantidade)
        return estoque_entrada


@api.post('/estoque-saida/', response=EstoqueSaidaSchema)
def estoque_saida(request, nf: int, qtd: int, product_id: int):
    product = Product.objects.filter(pk=product_id)
    if product:
        estoque_saida = EstoqueSaida.objects.create(nf=nf, movimento='s', produto_id=product_id, quantidade=qtd)
        qtd_atual = Product.objects.get(pk=product_id).estoque
        Product.objects.filter(pk=product_id).update(estoque=qtd_atual - estoque_saida.quantidade)
        return estoque_saida
