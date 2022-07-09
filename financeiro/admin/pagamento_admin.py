from django.contrib import admin
from ..models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
  list_display= [
    "id",
    "valor",
    "dataCriacao",
    "reserva",
  ]
  
  search_fields= [
    "id",
    "valor",
    "dataCriacao",
    "reserva",
  ]

  list_filter= [
    "dataCriacao",
    "reserva",
  ]

  fields= [
    "valor",
  ]

  def has_change_permission(self, request, obj= None):
    return False

  def has_delete_permission(self, request, obj= None):
    return False

  def has_add_permission(self, request):
    return False