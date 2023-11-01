from product import models
from django.contrib import admin
from django.utils.html import format_html

# admin.site.register(models.Product)
admin.site.register(models.Color)
admin.site.register(models.Size)


# admin.site.register(models.Image)


class ImageProductAdmin(admin.ModelAdmin):
    list_display = ['image_tag']

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(
                obj.image.url))


class ImageInline(admin.TabularInline):
    model = models.Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Image, ImageProductAdmin)
