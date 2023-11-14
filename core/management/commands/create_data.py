from django.shortcuts import get_object_or_404
from django.core.management.base import BaseCommand
from product.models import Product, Image, Color, Size


IMAGES = (
    {
        'color': 'yellow',
        'sizes': ['P', 'M', 'G', 'GG']
    },
    {
        'color': 'blue',
        'sizes': ['P', 'M', 'G']
    },
    {
        'color': 'black',
        'sizes': ['P', 'M']
    },
    {
        'color': 'red',
        'sizes': ['M', 'G']
    },
)

SIZES = ['P', 'M', 'G', 'GG']


def create_product():
    product, _ = Product.objects.get_or_create(
        name='Camiseta',
        price=120
    )

    for size in SIZES:
        Size.objects.get_or_create(size=size)

    for image in IMAGES:
        color_value = image['color']
        color, _ = Color.objects.get_or_create(color=color_value)

        for size_value in image['sizes']:
            size = get_object_or_404(Size, size=size_value)
            Image.objects.create(
                product=product,
                color=color,
                size=size,
            )


class Command(BaseCommand):
    help = "Cria produtos."

    def handle(self, *args, **options):
        create_product()
