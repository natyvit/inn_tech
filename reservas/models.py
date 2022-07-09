from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Quarto(models.Model):
  """
  Esta classe é responsável por todas as funcionalidades de quartos.
  """
  numero = models.IntegerField(
    verbose_name= "Número",
    unique= True,
    help_text= "*",
  )

  capacidade = models.IntegerField(
    verbose_name= "Capacidade",
    help_text= "*",
  )

  descricao = models.TextField(
    verbose_name= "Descrição",
    null= True,
    blank= True,
  )

  ocupacao = models.BooleanField(
    verbose_name= "Ocupação",
    default= False,
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

    super(Quarto, self).save(*args, **kwargs)

  def __str__(self):
     return f"Quarto {self.numero}"

  class Meta:
    app_label= "reservas"
    verbose_name= "Quarto"
    verbose_name_plural= "Quartos"

class Hospede(models.Model):
class Reserva(models.Model):
