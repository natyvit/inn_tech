from django.db import models

class Pagamento(models.Model):
  """
  Esta classe é responsável para armazenar/gerênciar todos os Pagamentos.
  """
  valor = models.DecimalField(
    verbose_name= "Valor",
    max_digits= 7,
    decimal_places= 2,
  )

  dataCriacao = models.DateTimeField(
    verbose_name= "Data Criação",
    auto_now_add= True,
  )

  reserva = models.ForeignKey(
    "reservas.Reserva",
    verbose_name= "Reserva",
    null= True,
    blank= True,
    on_delete= models.CASCADE,
  )

  def __str__(self):
    return f"Pagamento {self.id}"

  class Meta:
    app_label= "financeiro"
    verbose_name= "Pagamento"
    verbose_name_plural= "Pagamentos"