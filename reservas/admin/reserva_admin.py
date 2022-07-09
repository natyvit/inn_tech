from django.contrib import admin
from ..models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
  list_display= [
    "id",
    "dataChegada",
    "dataSaida",
    "valorReserva",
    "pagamentoConfirmado",
    "observacoes",
    "quarto",
  ]

  search_fields= [
    "id",
    "dataChegada",
    "dataSaida",
    "valorReserva",
    "pagamentoConfirmado",
    "observacoes",
    "quarto__numero",
  ]

  list_filter= [
    "dataChegada",
    "dataSaida",
    "pagamentoConfirmado",
  ]

  autocomplete_fields= [
    "quarto",
  ]