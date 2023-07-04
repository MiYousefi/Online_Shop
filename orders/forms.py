from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['firstname', 'lastname', 'phone_number', 'address', 'order_notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'order_notes': forms.Textarea(attrs={'rows': 4, 'placeholder': _('If you have any notes please enter here')}),

        }
