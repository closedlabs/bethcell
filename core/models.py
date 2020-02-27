from django.db import models
from django.db.models import Count
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from core.utils import unique_slug_generator
from django.urls import reverse
from core.choices import SEXO_CHOICES,CATEGORIA_CHOICES,ESCOLARIDADE,UF,DIAS,CELULA_CHOICES,EVASAO


class Celula(models.Model):
    nome        = models.CharField(verbose_name='Nome do Grupo', max_length=100, blank=True)
    lider       = models.OneToOneField('members.Lider',on_delete=models.CASCADE)
    colider     = models.CharField(verbose_name='Trainee', max_length=35)
    celula_de   = models.CharField(verbose_name='Célula de', max_length=1, choices=CELULA_CHOICES)
    criado_em   = models.DateField(verbose_name='Data de Abertura')
    dia_reuniao = models.TextField(verbose_name='Dia da Reunião',choices=DIAS)
    #endereço
    uf          = models.CharField('UF',max_length=2, choices=UF,blank=True)
    cidade      = models.CharField(max_length=50,verbose_name='Cidade',blank=True)
    rua         = models.CharField('Rua',max_length=100,blank=True)
    numero      = models.CharField('Numero',max_length=100,blank=True)
    bairro      = models.CharField('Bairro',max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Celula'
        verbose_name_plural = 'Celulas'

    def __str__(self):
        return str(self.lider) + ' Célula--' + str(self.nome)


class Evasao(models.Model):
    #dados pessoais
    nome           = models.CharField(verbose_name='Nome*',null=True ,max_length=40, unique=True)
    sexo           = models.CharField(verbose_name='Sexo*', max_length=1, choices=SEXO_CHOICES,null=True)
    nascimento     = models.DateField(verbose_name='Data de nascimento*',blank=True,null=True)
   
    tipo           = models.CharField(verbose_name='Situação Ministerial*', max_length=2,
        blank=True,null=True,choices=CATEGORIA_CHOICES)
    data_conversao = models.DateField(verbose_name='Data da Conversão',blank=True,null=True)
    data_encontro  = models.DateField(verbose_name='Data Do Encontro', blank=True, null=True)
    data_batismo   = models.DateField(verbose_name='Data Do Batismo', blank=True, null=True)
    consolidador   = models.CharField(verbose_name='Consolidador', max_length=40, blank=True)
    lider          = models.ForeignKey('members.Lider', on_delete=models.CASCADE,blank=True,null=True)
    date_delete    = models.DateTimeField(auto_now_add=True)
    motivo         = models.CharField(verbose_name='Motivo*',max_length=40,blank=True)
    
    def __str__(self):
        return self.nome

@receiver(post_delete, sender='members.Discipulo')
def create_conta(sender, instance, **kwargs):
    if instance:
        Evasao.objects.create(
        nome=instance,
        sexo=instance.sexo,
        motivo=instance.saiu
    )
            
def save_conta(sender, instance, **kwargs):
    instance.evasao.save()
  