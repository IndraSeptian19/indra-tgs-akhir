from django.db import models
from django.utils.translation import gettext_lazy as _
import os
# Create your models here.
class Aksara(models.Model):
    gambar = models.ImageField(_("gambar"), upload_to='aksaratot')
    class Meta:
        verbose_name = "gambar"
        verbose_name_plural = "gambar"

    def __str__(self):
        return str(os.path.split(self.image.path)[-1])