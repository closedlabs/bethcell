# Generated by Django 2.1 on 2019-04-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_evasao_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evasao',
            name='motivo',
            field=models.CharField(blank=True, max_length=40, verbose_name='Motivo*'),
        ),
    ]
