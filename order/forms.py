from django.forms import ModelForm

from staff.models import ItemInCart


class ItemInCartForm(ModelForm):
    class Meta:
        model = ItemInCart
        fields = ['quantity']
