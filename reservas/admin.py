from django.contrib import admin
from .models import Quarto

# Register your models here.

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