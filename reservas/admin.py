from django.contrib import admin
from .models import Quarto
from .models import Reserva

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

  @admin.register(Reserva)
  class ReservaAdmin(admin.ModelAdmin):
    list_display= [
      "id",
      "dataChegada",
      "dataSaida",
      "valorReserva",
      "pagamentoConfirmado",
      "observacoes",
    ]