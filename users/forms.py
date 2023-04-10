from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','avatar' ,'password1', 'password2')

class UserProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username', 'email', 'avatar')