# Generated by Django 3.2.11 on 2022-11-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_transfer_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='value',
            field=models.FloatField(verbose_name='Количество'),
        ),
    ]
