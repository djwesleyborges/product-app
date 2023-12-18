from django.contrib import admin

from .models import (
    EstoqueEntrada,
    EstoqueSaida
)


@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    ...


@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    ...

