from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart


@login_required()
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _('You can not proceed to checkout page because your cart is empty'))
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,

                )

            cart.clear()

            request.user.first_name = order_obj.firstname
            request.user.last_name = order_obj.lastname
            request.user.save()
            messages.success(request, _('Your order has successfully placed'))

    return render(request, 'orders/order_create.html', context={'form': order_form})
