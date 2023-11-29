from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
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
    #sizes = Product.objects.filter(color__color=color).distinct()
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


@api.post('/upload', url_name='upload')
def upload(request, file: UploadedFile = File(...)):
    data = file.read().decode()
    return {
        'name': file.name,
        'data': data
    }
