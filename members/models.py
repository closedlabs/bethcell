from django.db import models
from django.conf import settings
from core.choices import SEXO_CHOICES,CATEGORIA_CHOICES,ESCOLARIDADE,UF,DIAS,CELULA_CHOICES,EVASAO
from core.utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver

class Membro(models.Model):
    #dados pessoais
    nome           = models.CharField(verbose_name='Nome*',null=True ,max_length=100, unique=True)
    slug           = models.SlugField(blank=True,unique=True)
    sexo           = models.CharField(verbose_name='Sexo*', max_length=1, choices=SEXO_CHOICES,null=True)
    nascimento     = models.DateField(verbose_name='Data de nascimento*',blank=True,null=True)
    #contato
    email          = models.EmailField(blank=True)
    telefone       = models.CharField(verbose_name='Telefone/Cel', max_length=15,blank=True)
    facebook       = models.CharField(verbose_name='Facebook', max_length=50,blank=True)
    #sobre
    tipo           = models.CharField(verbose_name='Situação Ministerial*', max_length=2,
        blank=True,null=True,choices=CATEGORIA_CHOICES)
    data_conversao = models.DateField(verbose_name='Data da Conversão',blank=True,null=True)
    data_encontro  = models.DateField(verbose_name='Data Do Encontro', blank=True, null=True)
    data_batismo   = models.DateField(verbose_name='Data Do Batismo', blank=True, null=True)
    consolidador   = models.CharField(verbose_name='Consolidador', max_length=40, blank=True)
    escolaridade   = models.CharField(max_length=3,choices=ESCOLARIDADE,blank=True)
    profissao      = models.CharField(verbose_name='Profissão',max_length=40,
        help_text="Digite sua Ocupação",blank=True)
    #endereço
    uf             = models.CharField('UF',max_length=2, choices=UF,blank=True)
    cidade         = models.CharField(max_length=50,verbose_name='Cidade',blank=True)
    rua            = models.CharField('Rua',max_length=100,blank=True)
    numero         = models.CharField('Numero',max_length=100,blank=True)
    bairro         = models.CharField('Bairro',max_length=100, blank=True, null=True)
    complemento    = models.CharField(max_length=50,blank=True)
    cep            = models.CharField('CEP',max_length=20,blank=True)
    saiu           = models.CharField(verbose_name='Motivo*',max_length=40,blank=True,null=True)

    class Meta:
        abstract = True


class Lider(Membro):
    user          = models.OneToOneField(settings.AUTH_USER_MODEL,
    	on_delete=models.CASCADE, related_name='user')
    lider_de_rede = models.ForeignKey("self",verbose_name='Lider*',on_delete=models.CASCADE,
    blank=True,null=True, related_name="liderado")

    class Meta:
        verbose_name = 'Lider'
        verbose_name_plural = 'Lideres'

    def __str__(self):
        return str(self.user.first_name).upper() + ' ' + str(self.user.last_name).upper()

#gera um slug randomico
def leader_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(leader_pre_save_receiver,sender=Lider)

#signals para criar um lider quando um user é inserido
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Lider.objects.create(
            user=instance,
            nome=instance.first_name +' '+ instance.last_name,
    )
    instance.user.save()

class Discipulo(Membro):
    lider      = models.ForeignKey(Lider, on_delete=models.CASCADE,blank=True,null=True)
    celula     = models.ForeignKey('core.Celula', on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
    	verbose_name = 'Discipulo'
    	verbose_name_plural = 'Discipulos'

    def __str__(self):
        return self.nome
