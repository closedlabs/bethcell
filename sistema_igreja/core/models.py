from django.db import models
from core.choices import SEXO_CHOICES,CATEGORIA_CHOICES,ESCOLARIDADE,UF,DIAS,CELULA_CHOICES,EVASAO
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save,post_delete
from django.dispatch import receiver
from core.utils import unique_slug_generator
from django.urls import reverse
from django.db.models import Count

class Igreja(models.Model):
    nome = models.CharField(max_length=70, blank=True)
    
class Celula(models.Model):
    nome        = models.CharField(verbose_name='Nome do Grupo', max_length=35, blank=True)
    lider       = models.OneToOneField('Lider',on_delete=models.CASCADE)
    colider     = models.CharField(verbose_name='Trainee', max_length=35)
    celula_de   = models.CharField(verbose_name='Célula de', max_length=1, choices=CELULA_CHOICES)
    criado_em   = models.DateField(verbose_name='Data de Abertura')
    dia_reuniao = models.TextField(verbose_name='Dia da Reunião',choices=DIAS)
    #endereço
    uf             = models.CharField('UF',max_length=2, choices=UF,blank=True)
    cidade         = models.CharField(max_length=50,verbose_name='Cidade',blank=True)
    rua            = models.CharField('Rua',max_length=100,blank=True)
    numero         = models.CharField('Numero',max_length=100,blank=True)
    bairro         = models.CharField('Bairro',max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Celula'
        verbose_name_plural = 'Celulas'

    def __str__(self):
        return str(self.lider) + ' Célula--' + str(self.nome)

        
class Membro(models.Model):
    #dados pessoais
    nome           = models.CharField(verbose_name='Nome*',null=True ,max_length=40, unique=True)
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
    saiu           =  models.CharField(verbose_name='Motivo*',max_length=40,blank=True,null=True)
    class Meta:
        abstract = True


class Discipulo(Membro):
    lider      = models.ForeignKey('Lider', on_delete=models.CASCADE,blank=True,null=True)
    celula     = models.ForeignKey('Celula', on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.nome

def discipulo_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(discipulo_pre_save_receiver,sender=Discipulo)

class Lider(Membro):
    user          = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user')
    lider_de_rede = models.ForeignKey("self",verbose_name='Lider*',on_delete=models.CASCADE,
    blank=True,null=True, related_name="liderado")

    def __str__(self):
        return str(self.user) 

    #def get_absolute_url(self):
        #return reverse('products:detail',kwargs={'slug':self.slug})

def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver,sender=Lider)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):

    if created:
        Lider.objects.create(
            user=instance,
            nome=instance.first_name +' '+ instance.last_name,
    )
    instance.user.save()

@receiver(post_delete, sender=Lider)
def auto_delete(sender, instance, **kwargs):
    instance.user.delete()


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
    lider          = models.ForeignKey('Lider', on_delete=models.CASCADE,blank=True,null=True)
    date_delete    = models.DateTimeField(auto_now_add=True)
    motivo         = models.CharField(verbose_name='Motivo*',max_length=40,blank=True)
    
    def __str__(self):
        return self.nome

@receiver(post_delete, sender=Discipulo)
def create_conta(sender, instance, **kwargs):
    if instance:
        Evasao.objects.create(
        nome=instance,
        sexo=instance.sexo,
        motivo=instance.saiu
    )
            
def save_conta(sender, instance, **kwargs):
    instance.evasao.save()
  