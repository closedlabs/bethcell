# Generated by Django 2.2.3 on 2020-09-06 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_celula_cep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField(verbose_name='Data Da Reunião')),
                ('amount_member_present', models.PositiveIntegerField(default=0, verbose_name='Nº  De Presentes')),
                ('amount_decicions', models.PositiveIntegerField(default=0, verbose_name='Nº  De Decisões')),
                ('amount_visitors', models.PositiveIntegerField(default=0, verbose_name='Nº  De Visitantes')),
                ('observation', models.TextField(blank=True, verbose_name='Observação')),
                ('cell', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Celula')),
            ],
        ),
    ]