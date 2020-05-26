from django.db import models
from django.db.models import Count
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from core.utils import unique_slug_generator
from django.urls import reverse
from core.choices import SEXO_CHOICES,CATEGORIA_CHOICES,ESCOLARIDADE,UF,DIAS,CELULA_CHOICES,EVASAO


class Celula(models.Model):
    name          = models.CharField(verbose_name='Nome do Grupo', max_length=100, blank=True)
    leader        = models.OneToOneField('members.Lider',on_delete=models.CASCADE)
    coleader      = models.CharField(verbose_name='Trainee', max_length=35)
    cell_type     = models.CharField(verbose_name='Célula de', max_length=1, choices=CELULA_CHOICES)
    created_at    = models.DateField(verbose_name='Data de Abertura')
    meeting_day   = models.TextField(verbose_name='Dia da Reunião',choices=DIAS)
    #endereço
    uf            = models.CharField('UF',max_length=2, choices=UF,blank=True)
    city          = models.CharField(max_length=50,verbose_name='Cidade',blank=True)
    street        = models.CharField('Rua',max_length=100,blank=True)
    number        = models.CharField('Numero',max_length=100,blank=True)
    neighborhood  = models.CharField('Bairro',max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Celula'
        verbose_name_plural = 'Celulas'

    def __str__(self):
        return str(self.leader) + ' Célula--' + str(self.name)


class Evasao(models.Model):
    #dados pessoais
    name                    = models.CharField(verbose_name='Nome*',null=True ,max_length=40, unique=True)
    sex                     = models.CharField(verbose_name='Sexo*', max_length=1, choices=SEXO_CHOICES,null=True)
    birth                   = models.DateField(verbose_name='Data de nascimento*',blank=True,null=True)
   
    ministerial_situation   = models.CharField(verbose_name='Situação Ministerial*', max_length=2,
        blank=True,null=True,choices=CATEGORIA_CHOICES)
    date_conversion         = models.DateField(verbose_name='Data da Conversão',blank=True,null=True)
    meeting_date           = models.DateField(verbose_name='Data Do Encontro', blank=True, null=True)
    date_batismo            = models.DateField(verbose_name='Data Do Batismo', blank=True, null=True)
    consolidator            = models.CharField(verbose_name='Consolidador', max_length=40, blank=True)
    leader                  = models.ForeignKey('members.Lider', on_delete=models.CASCADE,blank=True,null=True)
    date_delete             = models.DateTimeField(auto_now_add=True)
    reason                  = models.CharField(verbose_name='Motivo*',max_length=40,blank=True)
    
    def __str__(self):
        return self.name

@receiver(post_delete, sender='members.Discipulo')
def create_conta(sender, instance, **kwargs):
    if instance:
        Evasao.objects.create(
        name=instance,
        sex=instance.sex,
        reason='saiu'
    )
            
def save_conta(sender, instance, **kwargs):
    instance.evasao.save()
  