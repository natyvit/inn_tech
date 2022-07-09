from django.contrib import admin
from ..models import Quarto

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
  list_display= [
    "id",
    "numero",
    "capacidade",
    "descricao",
    "ocupacao",
    "usuario_criacao",
  ]

  search_fields= [
    "id",
    "numero",
    "capacidade",
    "descricao",
    "ocupacao",
    "usuario_criacao__username",
  ]

  list_filter= [
    "ocupacao",
    "usuario_criacao",
  ]

  autocomplete_fields= [
    "usuario_criacao",
  ]