from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from estoque.models import EstoqueItem, Estoque
from estoque.schema import EstoqueSchema
from product.models import Product, Color, Size
from product import schema

api = NinjaAPI()


@api.get('/product/colors/', response=List[schema.ColorSchema])
def colors(request):
    return Color.objects.all()


@api.get('/product/{color}/sizes/', response=List[schema.SizeSchema])
def get_sizes(request, color: str):
    color = get_object_or_404(Color, color=color)
    sizes = Size.objects.filter(product__color=color).distinct()
    return sizes


@api.get('/product/{color}/{size}/image/', response=schema.ProductSchema)
def get_product_by_color_size(request, color: str, size: str):
    color = get_object_or_404(Color, color=color)
    size = get_object_or_404(Size, size=size)
    return Product.objects.filter(color=color, size=size).first()


@api.get('/product', response=List[schema.ProductSchema])
def products(request, size: Optional[str] = None):
    if size:
        return Product.objects.filter(image__image__name=size)
    return Product.objects.all()


@api.get('/product/{product_id}', response={200: schema.ProductSchema, 404: schema.NotFoundSchema})
def product(request, product_id: str):
    product = get_object_or_404(Product, id=product_id)
    return product


@api.get('/products/{color}/{size}/', response=List[schema.ProductSchema])
def get_similar_products(request, color: str, size: str):
    color = get_object_or_404(Color, color=color)
    size = get_object_or_404(Size, size=size)
    return Product.objects.filter(color=color, size=size)


@api.post('/estoque-entrada/', response=EstoqueSchema)
def estoque_entrada(request, product_list: EstoqueSchema):
    product = Product.objects.filter(pk=product_list.estoque_item[0].produto).first()
    if product:
        estoque_entrada = Estoque.objects.create(nf=product_list.nf, movimento='e')
        qtd_atual = Product.objects.get(pk=product_list.estoque_item[0].produto).estoque
        Product.objects.filter(pk=product_list.estoque_item[0].produto).update(
            estoque=qtd_atual + product_list.estoque_item[0].quantidade)
        estoque_item = EstoqueItem.objects.create(estoque=estoque_entrada, produto=product,
                                                  quantidade=qtd_atual + product_list.estoque_item[0].quantidade)
    return estoque_item.estoque


@api.post('/estoque-saida/', response=EstoqueSchema)
def estoque_saida(request, product_list: EstoqueSchema):
    product = Product.objects.filter(pk=product_list.estoque_item[0].produto).first()
    if product:
        estoque_saida = Estoque.objects.create(nf=product_list.nf, movimento='s')
        qtd_atual = Product.objects.get(pk=product_list.estoque_item[0].produto).estoque
        Product.objects.filter(pk=product_list.estoque_item[0].produto).update(
            estoque=qtd_atual - product_list.estoque_item[0].quantidade)
        estoque_item = EstoqueItem.objects.create(estoque=estoque_saida, produto=product,
                                                  quantidade=qtd_atual - product_list.estoque_item[0].quantidade)
    return estoque_item.estoque
