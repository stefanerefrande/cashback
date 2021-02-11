from django.db import models


class Pedidos(models.Model):

    id_pedidos = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    valor_total = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    porcentagem_cashback = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    data = models.DateField(
        max_length=10,
        null=False,
        blank=False
    )

    status = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    id_revendedor = models.ForeignKey(
        'Revendedores.Revendedores',
        on_delete= models.CASCADE
    )




