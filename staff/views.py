from django.shortcuts import render, redirect

from .forms import StaffForm, StorageStaffForm, AddressForm, FullnameForm, StorageForm, ProductForm
from .models import StorageStaff, Fullname, Product


# Create your views here.
def list_staff(request):
    staffs = StorageStaff.objects.all()
    return render(request, 'staffs.html', {'staffs': staffs})


def create_staff(request):
    if request.method == 'POST':
        forms = {
            'full_name_form': FullnameForm(request.POST or None),
            'storage_staff_form': StorageStaffForm(request.POST or None),
            'addresses_form': AddressForm(request.POST or None),
        }

        if forms['full_name_form'].is_valid() and forms['addresses_form'].is_valid() and forms[
            'storage_staff_form'].is_valid():
            full_name = forms['full_name_form'].save()
            # TODO : Only show address of a storage
            address = forms['addresses_form'].save()
            storage_staff = forms['storage_staff_form'].save(commit=False)
            storage_staff.fullname = full_name
            storage_staff.address = address
            storage_staff.save()

        return redirect('list_staff')

    else:
        forms = {
            'full_name_form': FullnameForm(),
            'storage_staff_form': StorageStaffForm(),
            'addresses_form': AddressForm(),
        }

        return render(request, 'staff_create.html', {'forms': forms})


# def search_products(request, **kwargs):
#     if request.method != 'POST':
#         product = Product.objects.all()
#         return render(request, 'products.html', {'products': product})
#     else:
#         products = Product.objects.filter(**kwargs)
#         return render(request, 'products.html', {'products': products})


def get_products(request):
    if request.method != 'POST':
        product = Product.objects.all()
        return render(request, 'products.html', {'products': product})
    else:
        products = Product.objects.filter(name__icontains=request.POST['product_search'])
        return render(request, 'products.html', {'products': products})


def create_product(request):
    product_form = ProductForm(request.POST or None)

    if product_form.is_valid():
        product_form.save()

        return redirect('search_products')

    return render(request, 'product_create.html', {'forms': product_form})


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_form = ProductForm(request.POST or None, instance=product)

    if product_form.is_valid():
        product_form.save()

        return redirect('search_products')

    return render(request, 'product_create.html', {'forms': product_form, 'product': product})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('search_products')

