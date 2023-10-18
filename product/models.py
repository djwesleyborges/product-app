from django.db import models
from django.utils.translation import gettext_lazy as _


class Color(models.Model):
    color = models.CharField(max_length=100, verbose_name=_('Color Name'))

    def __str__(self):
        return self.color


class Size(models.Model):
    size = models.CharField(max_length=100, verbose_name=_('Size Name'))

    def __str__(self):
        return self.size


class Product(models.Model):
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    name = models.CharField(
        max_length=100,
        verbose_name=_('name'),
        help_text=_('Provide the name of the product'),
        null=False,
        blank=False, )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name=_('price'),
        help_text=_('Provide the price of the product'),
        null=False,
        blank=False, )

    colors = models.ManyToManyField(Color, verbose_name=_('Colors'))

    size = models.ManyToManyField(Size, verbose_name=_('Sizes'))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Product name={self.name} />'
