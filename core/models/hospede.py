from django.db import models


class Hospede(models.Model):
    """
    Esta classe serve para armazenarmos os hóspedes do sistema.
    """
    nome = models.CharField(
        verbose_name="Nome",
        max_length=30,
        help_text="*Campo Obrigatório",
    )

    telefone = models.CharField(
        verbose_name="Telefone",
        max_length=30,
        help_text="*Campo Obrigatório",
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "core"
        verbose_name = "Hóspede"
        verbose_name_plural = "Hóspedes"
