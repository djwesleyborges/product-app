from django.contrib import admin

from . import models
from .models import EstoqueItem


class EstoqueItemInline(admin.TabularInline):
    model = EstoqueItem
    extra = 0


@admin.register(models.EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItemInline,)


@admin.register(models.EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItemInline,)
