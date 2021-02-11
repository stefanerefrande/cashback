from django.db import models

class Pedidos(models.Model):

    IDPedidos = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    Valor_Total = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    Porcentagem_Cashback = models.PositiveIntegerField(
        null=False,
        blank=False
    )

    Data = models.DateField(
        max_length=10,
        null=False,
        blank=False
    )

    Status = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    IDRevendedor = models.ForeignKey(
        'Revendedores.Revendedores',
        on_delete= models.CASCADE
    )




objetos = models.Manager()