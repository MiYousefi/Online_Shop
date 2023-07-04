from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(_('Is Paid?'), default=False)

    firstname = models.CharField(_('First Name'), max_length=100)
    lastname = models.CharField(_('last Name'), max_length=100)
    phone_number = models.CharField(_('Phone Number'), max_length=15)
    address = models.CharField(_('Address'), max_length=700)

    order_notes = models.CharField(_('Order Note'), max_length=700, blank=True)

    datetime_created = models.DateTimeField(_('Datetime Created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Datetime Modified'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('Order'))
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_items', verbose_name=_('Product'))
    quantity = models.PositiveIntegerField(_('Quantity'), default=1)
    price = models.PositiveIntegerField(_('Price'))

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} * {self.quantity} (Price: {self.price})'
