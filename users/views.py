from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.urls import reverse

from .models import User
from .forms import RegistrationForm, UserProfileForm
from django.conf import settings

from product.models import Basket
# Create your views here.

class LoginView(LoginView):
    template_name = 'registration/registration.html'

    def get_success_url(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        else:
            return render(request, self.template_name, {'username' : username})
    
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if 'avatar' in request.FILES:
                avatar = request.FILES['avatar']
                fs = FileSystemStorage(location =settings.MEDIA_ROOT + '/profile_images' )#Указ директории
                filename = fs.save(avatar.name, avatar)
                user.avatar = 'profile_images/' + filename
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)            
            messages.add_message(request, messages.SUCCESS, 'Вы успешно зарегистрированы!')

    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse, 'users/profile.html')
    else:
        form = UserProfileForm(instance = request.user)
    context = {
        'form' : form,
        'baskets' : Basket.objects.all
    }    

    return render(request, 'registration/profile.html', context=context)