#@Author   ：Htojk
#@Time     :2018/10/8  19:57
#@Software :PyCharm

from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SelfDefineUser(UserCreationForm):
    昵称=forms.CharField(max_length=50,required=False)
    class Meta:
        model=User
        fields=('username','password1','password2','email','昵称')

class SelfDefineChangeMessage(UserChangeForm):
    昵称 = forms.CharField(max_length=50, required=False)
    class Meta:
        model = User
        fields = ('username', 'password', 'email', '昵称')