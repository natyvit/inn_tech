from django.contrib import admin
from ..models import Saida

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
  list_display= [
    "id",
    "valor",
    "dataCriacao",
    "motivo",
    "observacoes",
    "usuario_criacao",
  ]