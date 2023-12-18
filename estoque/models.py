from django.contrib.auth.models import User
from django.db import models

from core.models import TimeStampedModel
from product.models import Product

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Estoque(TimeStampedModel):
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.nf:
            return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
        return '{} --- {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))

    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '---'


class EstoqueEntrada(Estoque):
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    # saldo = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'


class EstoqueSaida(Estoque):
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    # saldo = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'estoque saída'
        verbose_name_plural = 'estoque saída'
