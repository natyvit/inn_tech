from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Reserva


@receiver(post_save, sender=Reserva)
def reserva_post_save(sender, instance, created, **kwargs):
    if created:
        instance.gerar_pagamento_se_confirmado()
    elif kwargs["update_fields"]:
        if "pagamentoConfirmado" in kwargs["update_fields"]:
            instance.gerar_pagamento_se_confirmado()
