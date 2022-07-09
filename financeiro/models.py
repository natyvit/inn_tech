from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

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

class Saida(models.Model):
  """
  Esta classe é responsável por todas as funcionalidades de saídas.
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

  motivo = models.TextField(
    verbose_name= "Motivo",
  )

  observacoes = models.TextField(
    verbose_name= "Observações",
    null= True,
    blank= True,
  )

  usuario_criacao = models.ForeignKey(
    User,
    verbose_name= "Usuário Criação",
    null= True,
    blank= True,
    on_delete= models.SET_NULL,
  )

  def save(self, *args, **kwargs):
    user = get_current_user()
    if user and not user.pk:
        user = None
    if not self.pk:
        self.usuario_criacao = user

    super(Saida, self).save(*args, **kwargs)

    def __str__(self):
     return f"Saida {self.id}"

  class Meta:
    app_label= "financeiro"
    verbose_name= "Saída"
    verbose_name_plural= "Saídas"
