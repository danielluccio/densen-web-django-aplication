from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    updated_at = models.DateTimeField(verbose_name='atualizado_em', auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        db_table = 'usuarios'
        ordering = ['-id']

    def __str__(self):
        return self.get_full_name