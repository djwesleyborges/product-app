from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from product.models import Product
from schema import ProductSchema, NotFoundSchema

api = NinjaAPI()


@api.get('/product', response=List[ProductSchema])
def products(request, name: Optional[str] = None):
    if name:
        return Product.objects.filter(name__icontains=name)
    return Product.objects.all()


@api.get('/product/{product_id}', response={200: ProductSchema, 404: NotFoundSchema})
def product(request, product_id: str):
    product = get_object_or_404(Product, id=product_id)
    return product

