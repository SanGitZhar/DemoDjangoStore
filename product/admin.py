from django.contrib import admin
from .models import Products, Basket, ProductCategory

admin.site.register(Products)
admin.site.register(Basket)
admin.site.register(ProductCategory)
