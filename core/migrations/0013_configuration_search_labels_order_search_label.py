# Generated by Django 4.0.4 on 2022-05-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_order_number_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='search_labels',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='search_label',
            field=models.BooleanField(default=False),
        ),
    ]
