from product.models import Color, Image, Product, Size
from django.contrib import admin
from django.utils.html import format_html


@admin.register(Image)
class ImageProductAdmin(admin.ModelAdmin):
    list_display = ['image_tag']

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(
                obj.image.url))


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Color)
admin.site.register(Size)
