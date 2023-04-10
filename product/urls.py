from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', products, name='products'),
    path('baskets/add/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('remove/remove/<int:basket_id>/', remove_from_basket, name = 'remove_from_basket'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)