from django.db import models

# Create your models here.
class Books(models.Model):
    Eunit=models.CharField(max_length=64)
    Elesson=models.CharField(max_length=64)
    Epoem=models.CharField(max_length=64)
    Eobj=models.CharField(max_length=64)

