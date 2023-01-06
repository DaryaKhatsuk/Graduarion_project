from django.db import models
from django.db.models.functions import datetime


class Cart(models.Model):
    idCart = models.AutoField(primary_key=True, verbose_name='Key')
    cartPlort = models.CharField(max_length=30, verbose_name='Plort', null=True)
    imagePlort = models.CharField(max_length=200, verbose_name='ImagePlort', null=True)
    cartPrice = models.IntegerField(verbose_name='Price', null=True)
    cartQuantity = models.IntegerField(verbose_name='Quantity', null=True)
    priceLine = models.IntegerField(verbose_name='Price line', null=True)
    totalPrice = models.IntegerField(verbose_name='Total price', null=True)

    deliveryAddress = models.CharField(max_length=30, verbose_name='Delivery address', null=True)

    ConsentDataProcessing = models.BooleanField(verbose_name='Consent to data processing', null=True)

    dateDelivery = models.DateField(null=True)
    dateOrder = models.DateField(unique_for_date=datetime.timezone.now, null=True)
    cartCustomer = models.CharField(max_length=120, verbose_name='Customer', null=True)

    def __str__(self):
        return f'{self.cartPlort}'

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ('cartPlort',)


class Purchase(models.Model):
    idPurchase = models.AutoField(primary_key=True, verbose_name='Key')
    boughtPlort = models.CharField(max_length=30, verbose_name='Plort')
    pricePlort = models.IntegerField(verbose_name='Price')
    boughtQuantity = models.IntegerField(verbose_name='Quantity')
    totalPrice = models.IntegerField(verbose_name='Total price')

    deliveryAddress = models.CharField(max_length=30, verbose_name='Delivery address')
    dateDelivery = models.DateField()

    currentCustomer = models.CharField(max_length=120, verbose_name='Customer')