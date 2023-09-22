from django.db import models

# Create your models here.


class Tabela(models.Model):
    title = models.CharField(max_length=5)
    vouf = models.BooleanField(default=False)
