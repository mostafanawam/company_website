from django.db import models

# Create your models here.


class Settings(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)


    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"