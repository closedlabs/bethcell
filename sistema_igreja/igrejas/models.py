from datetime import timedelta
from django.utils import timezone
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

def one_month_from_today():
    return timezone.now() + timedelta(days=30)


class Igreja(TenantMixin):
    nome       = models.CharField('Nome da Igreja/Cliente',max_length=100)
    pago_ate   = models.DateField('Pago Até',default=one_month_from_today, blank=True, null=True)
    on_trial   = models.BooleanField('Em Teste',default=True)
    criado_em  = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    pass