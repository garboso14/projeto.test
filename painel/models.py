from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(_("Nome"), max_length=250)
    