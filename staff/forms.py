from django import forms
from django.forms import inlineformset_factory

from staff.models import Staff, Person, StorageStaff, Address, Fullname, Storage, Product


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'sex',
            'age',
        ]


class StaffForm(PersonForm):
    class Meta(PersonForm.Meta):
        model = Staff
        fields = PersonForm.Meta.fields + ['workAddress']


class StorageStaffForm(StaffForm):
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['workAddress'].queryset = Address.objects.filter(id__in=Storage.objects.values('address_id'))

    class Meta(StaffForm.Meta):
        model = StorageStaff
        fields = StaffForm.Meta.fields + ['storage']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'fullAddress',
            'city',
            'country'
        ]


class FullnameForm(forms.ModelForm):
    class Meta:
        model = Fullname
        fields = [
            'firstname',
            'lastname'
        ]


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = [
            'address'
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'manufacturer'
        ]


AddStorageStaffForm = inlineformset_factory(Storage, StorageStaff, fk_name='storage', fields=('storage',))
