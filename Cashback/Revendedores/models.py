from django.db import models


class Revendedores(models.Model):


    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False,
    )

    senha = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    status = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default='Em validação'
    )



