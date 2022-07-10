from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Reserva


@receiver(post_save, sender=Reserva)
def reserva_post_save(sender, instance, created, **kwargs):
    if created:
        instance.gerar_pagamento_se_confirmado()
        instance.ocupar_quarto()
    elif kwargs["update_fields"]:
        mudou_pagamentoConfirmado = "pagamentoConfirmado" in kwargs["update_fields"]
        mudou_valorReserva = "valorReserva" in kwargs["update_fields"]

        if mudou_pagamentoConfirmado:
            instance.gerar_pagamento_se_confirmado()

        if mudou_valorReserva:
            instance.atualizar_valor_pagamento()
