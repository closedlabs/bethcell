from django.db import models
from django.contrib.auth.models import AbstractUser

#modelo de usuario customizado do django com novos campos
class CustomUser(AbstractUser):
    is_generation_leader = models.BooleanField('é Lider de Célula', default=False)
    is_cell_leader       = models.BooleanField('é Lider de Geração', default=False)
    is_teacher           = models.BooleanField('é Professor', default=False)

    def __str__(self):
        return self.username
