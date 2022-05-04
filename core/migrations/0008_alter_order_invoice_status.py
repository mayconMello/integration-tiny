# Generated by Django 4.0.3 on 2022-03-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_configuration_days_configuration_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='invoice_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pendente'), (2, 'Emitida'), (3, 'Cancelada'), (4, 'Enviada - Aguardando recibo'), (5, 'Rejeitada'), (6, 'Autorizada'), (7, 'Emitida DANFE'), (8, 'Registrada'), (9, 'Enviada - Aguardando protocolo'), (10, 'Denegada')], default=1),
        ),
    ]
