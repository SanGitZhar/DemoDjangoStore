from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import *
from django.contrib.auth.decorators import login_required
from users.models import User

# def index(request):
#     return render(request, 'product/index.html')


def products(request):
    context = {
        'categories': ProductCategory.objects.all(),
        'products': Products.objects.all()
    }
    return render(request, 'product/products.html', context)


@login_required
def add_to_basket(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))#Вернуть на текущую страницу
          

def remove_from_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


