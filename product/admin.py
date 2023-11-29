from product.models import Color, Product, Size
from django.contrib import admin
from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'name', 'price', 'image', 'color', 'size']
    extra = 0

    @staticmethod
    def image_tag(obj):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(
                obj.image.url))


admin.site.register(Color)
admin.site.register(Size)
