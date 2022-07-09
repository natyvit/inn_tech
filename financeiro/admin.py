from django.contrib import admin
from .models import Pagamento
from .models import Saida

# Register your models here.

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
  list_display= [
    "id",
    "valor",
    "dataCriacao",
    "reserva",
  ]
  
  def has_change_permission(self, request, obj= None):
    return False

  def has_delete_permission(self, request, obj= None):
    return False

  def has_add_permission(self, request):
    return False

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