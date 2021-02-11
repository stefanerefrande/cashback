from django.db import models


class Revendedores(models.Model):

    IDRevendedor = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    Nome = models.CharField(
        max_length=2147483647,
        null=False,
        blank=False
    )

    CPF = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    Email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )

    Senha = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    Status = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )




objetos = models.Manager()
