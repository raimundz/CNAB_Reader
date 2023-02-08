from django.db import models



class FileCNAB(models.Model):
  tipo = models.TextField(max_length=1)
  data = models.TextField(max_length=8)
  valor = models.TextField(max_length=10)
  natureza = models.TextField(max_length=10)
  CPF = models.TextField(max_length=11)
  cartao = models.TextField(max_length=12)
  hora = models.TextField(max_length=6)
  dono = models.TextField(max_length=14)
  loja = models.TextField(max_length=19)

