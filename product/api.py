from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from product.models import Product, Image
from product.schema import ProductSchema, NotFoundSchema, ImageSchema

api = NinjaAPI()


@api.get('/product/{product_id}/image/', response=List[ImageSchema])
def products_images(request, product_id: int, size: str = None):
    if size:
        product = get_object_or_404(Product, pk=product_id)
        images = Image.objects.filter(product=product, size__size=size)
        return images
    return Image.objects.filter(product=product)


@api.get('/product', response=List[ProductSchema])
def products(request, name: Optional[str] = None):
    if name:
        return Product.objects.filter(name__icontains=name)
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
