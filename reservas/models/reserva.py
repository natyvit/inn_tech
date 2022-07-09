from django.db import models
from .quarto import Quarto

class Reserva(models.Model):
  """
  Está classe é respondável por todas as funcionalidades de reservas.
  """
  dataChegada = models.DateTimeField(
    verbose_name= "Data Chegada",
    help_text= "*Campo Obrigatório",
  )

  dataSaida = models.DateTimeField(
    verbose_name= "Data Saída",
    null= True,
    blank= True,
  )

  valorReserva = models.DecimalField(
    verbose_name= "Valor da Reserva",
    help_text= "*Campo Obrigatório",
    max_digits= 7,
    decimal_places= 2,
  )

  pagamentoConfirmado = models.BooleanField(
    verbose_name= "Pagamento Confirmado",
    default= False,
  )

  observacoes = models.TextField(
    verbose_name= "Observações",
    null= True,
    blank= True,
  )

  quarto = models.ForeignKey(
    Quarto,
    verbose_name= "Quarto",
    null= True,
    blank= True,
    on_delete= models.SET_NULL,
  )

  def __str__(self):
    return f"Reserva {self.id}"

  class Meta:
    app_label= "reservas"
    verbose_name= "Reserva"
    verbose_name_plural= "Reservas"