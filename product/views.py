from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from order.forms import ItemInCartForm
from staff.models import *
from product.models import *


# Create your views here.
def home(request):
    items = Item.objects.all().order_by('-id')[:4]
    context = {
        'items': items,
        'page': 'home'
    }
    return render(request, 'index.html', context)


def detailProduct(request, product_id):
    item = Item.objects.get(pk=product_id)

    if request.method == 'POST':
        commnet = Comment(customer=request.user, item=item, content=request.POST['content'])
        commnet.save()

    product = item.product
    product.price = int(product.price)
    if product.type == 1:
        product = Clothing.objects.get(pk=product.id)
    elif product.type == 2:
        product = Book.objects.get(pk=product.id)
    else:
        product = Electronic.objects.get(pk=product.id)
    comments = Comment.objects.filter(item=item)

    context = {
        'item': item,
        'comments': comments,
        'products': product
    }

    return render(request, 'product_detail.html', context)


@login_required(login_url='/login')  # Check login
def add_to_cart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    item = Item.objects.get(pk=id)

    cart = current_user.cart
    if cart is None:
        cart = Cart(user=current_user, order=None)
        cart.save()

    data = ItemInCart.objects.get(cart=cart, item=item, order=None)  # Check product in shopcart
    if data is not None:
        control = 1
        # The product is in the cart
    else:
        control = 0  # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ItemInCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  shopcart
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else:  # Inser to Shopcart
                data = ItemInCart(item_id=id, cart=cart, quantity=request.POST['quantity'])
                data.save()
        messages.success(request, "Product added to Shopcart ")
        return HttpResponseRedirect(url)

    else:  # if there is no post
        if control == 1:  # Update  shopcart
            data = ItemInCart.objects.get(item_id=id, cart=cart, order=None)
            data.quantity += 1
            data.save()  #
        else:  # Inser to Shopcart
            data = ItemInCart(cart=cart, user=current_user)  # model ile bağlantı kur
            data.user_id = current_user.id
            data.item_id = id
            data.quantity = 1
            data.save()  #
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)


def shoppingCart(request):
    current_user = request.user  # Access User Session information
    cart = Cart.objects.filter(user=current_user, status=1)
    if len(cart) == 0:
        cart = Cart(user=current_user, status=1)
        cart.save()
    else:
        cart = Cart.objects.get(user=current_user, status=1)
    shopcart = ItemInCart.objects.filter(cart=cart, order=None)
    total = 0
    for rs in shopcart:
        total += rs.item.price * rs.quantity
    # return HttpResponse(str(total))
    context = {'shopcart': shopcart,
               'total': total,
               }
    return render(request, 'shopping_cart.html', context)


def order_item(request):
    current_user = request.user
    cart = Cart.objects.get(user_id=current_user.id, status=1)
    shopcart = ItemInCart.objects.filter(cart=cart, order=None)
    # address=Address.objects.get(pk=current_user.address)
    total = 0
    for rs in shopcart:
        total += rs.item.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        # return HttpResponse(request.POST.items())
        # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
        # ..............
        payment = Payment(amount=total, additionalFee=0)
        payment.save()
        order = Order(saleOff=0, payment=payment, customer=current_user, status_id=1)
        order.save()  #
        cart.status = 0
        cart.save()

        cart_new = Cart(user=current_user, status=1)
        # TODO : Remove from ProductInStock
        messages.success(request, "Your Order has been completed. Thank you ")
        return render(request, 'order_completed.html', {'order-code': order.id})

    context = {'shopcart': shopcart,
               'total': total,
               }
    return render(request, 'order_Form.html', context)


def search_items(request):
    if request.method != 'GET':
        items = Item.objects.all()
        return render(request, 'items.html', {'items': items})
    else:
        filters = {}
        if 'product_name' in request.GET:
            filters['product__name__icontains'] = request.GET['product_name']
        if 'price' in request.GET:
            range = request.GET['price']
            range = range.split('-')

            filters['price__gte'] = range[0].strip()[:-1]
            filters['price__lte'] = range[1].strip()[:-1]
        if 'type' in request.GET:
            filters['product__type'] = request.GET['type']

        items = Item.objects.filter(**filters)
        return render(request, 'items.html', {'items': items})

