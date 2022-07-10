from django.db import models
from global_functions import get_changes

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
    on_delete= models.SET_NULL,
  )

  @property
  def gerou_pagamento(self):
    return hasattr(self, "pagamento")

  def gerar_pagamento_se_confirmado(self):
    from financeiro.models import Pagamento

    nao_gerou_pagamento = not self.gerou_pagamento
    if self.pagamentoConfirmado and nao_gerou_pagamento:
      Pagamento.objects.create(
        valor=self.valorReserva,
        reserva=self,
      )

  def atualizar_valor_pagamento(self):
    if self.gerou_pagamento:
      self.pagamento.atualizar_valor(self.valorReserva)

  def save(self, *args, **kwargs):
    if self.pk:
      mudancas = get_changes(self)
      kwargs["update_fields"] = mudancas.normais

    super(Reserva, self).save(*args, **kwargs)

  def __str__(self):
    return f"Reserva {self.id}"

  class Meta:
    app_label= "reservas"
    verbose_name= "Reserva"
    verbose_name_plural= "Reservas"
