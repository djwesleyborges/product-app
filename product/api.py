from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from product.models import Product, Image, Color
from product.schema import ProductSchema, NotFoundSchema, ImageSchema, SizeSchema, \
    ColorSchema

api = NinjaAPI()


@api.get('/product/{int:productId}/image/{str:size}', response=List[ImageSchema])
def products_images(request, productId: int, size: str):
    if size:
        product = get_object_or_404(Product, pk=productId)
        images = Image.objects.filter(product=product, size__size=size)
        return images
    return Image.DoesNotExist()


# @api.get('/product/{int:productId}/color/{str:color}', response=List[ImageSchema])
# def get_product_by_color(request, productId: int, color: str):
#     if color:
#         product = get_object_or_404(Product, pk=productId)
#         image = Image.objects.filter(product=product, color__color=color)
#         return image
#     return Image.DoesNotExist()


@api.get('/product/{int:productId}/color/{str:color}', response=List[ColorSchema])
def get_product_by_color_size(request, productId: int, color: str):
    if color:
        product = get_object_or_404(Product, pk=productId)
        color = Color.objects.get(color=color).id
        color = Color.objects.filter(product=product, pk=color)
        return color
    return Color.DoesNotExist()


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
