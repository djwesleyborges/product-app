from django.db import models
from django.utils.translation import gettext_lazy as _


class Color(models.Model):
    color = models.CharField(_('Color Name'), max_length=100)

    def __str__(self):
        return self.color


class Size(models.Model):
    size = models.CharField(_('Size Name'), max_length=100)

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100,
        help_text=_('Provide the name of the product'),
        null=False,
        blank=False
    )

    price = models.DecimalField(
        _('price'),
        decimal_places=2,
        max_digits=5,
        help_text=_('Provide the price of the product'),
        null=False,
        blank=False
    )
    image = models.ImageField(upload_to='')
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    estoque = models.IntegerField('estoque atual', default=0)

    def __str__(self):
        return self.name
