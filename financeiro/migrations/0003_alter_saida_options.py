# Generated by Django 4.0.5 on 2022-07-09 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_alter_pagamento_datacriacao_alter_pagamento_valor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saida',
            options={'verbose_name': 'Saída', 'verbose_name_plural': 'Saídas'},
        ),
    ]
