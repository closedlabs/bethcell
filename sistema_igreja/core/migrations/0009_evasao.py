# Generated by Django 2.1 on 2019-04-08 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190404_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evasao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, null=True, unique=True, verbose_name='Nome*')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True, verbose_name='Sexo*')),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento*')),
                ('tipo', models.CharField(blank=True, choices=[('N0', 'Novo Convertido'), ('N1', 'Cursando-N1'), ('N2', 'Cursando-N2'), ('N3', 'Cursando-N3'), ('N4', 'Cursando-Trainee'), ('N5', 'Trainee Formado'), ('LC', 'Lider de Célula'), ('LG', 'Lider de Geração'), ('PR', 'Pastores')], max_length=2, null=True, verbose_name='Situação Ministerial*')),
                ('data_conversao', models.DateField(blank=True, null=True, verbose_name='Data da Conversão')),
                ('data_encontro', models.DateField(blank=True, null=True, verbose_name='Data Do Encontro')),
                ('data_batismo', models.DateField(blank=True, null=True, verbose_name='Data Do Batismo')),
                ('consolidador', models.CharField(blank=True, max_length=40, verbose_name='Consolidador')),
                ('date_delete', models.DateTimeField(auto_now_add=True)),
                ('lider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Lider')),
            ],
        ),
    ]
