from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('registration/',registration,name='registration'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),

]