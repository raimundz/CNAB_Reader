from django.db import models


class FileCNAB(models.Model):
  tipo = models.IntegerField(max_length=1)
  data = models.TextField(max_length=8)
  valor = models.IntegerField(max_length=10)
  CPF = models.IntegerField(max_length=11)
  cartão = models.IntegerField(max_length=12)
  hora = models.IntegerField(max_length=6)
  dono = models.TextField(max_length=14)
  loja = models.TextField(max_length=19)

