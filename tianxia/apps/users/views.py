from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth import login,logout,authenticate
from . import forms,models
from django.contrib.auth.decorators import login_required
from apps.index.models import show_pictures_index
# Create your views here.


def Index_view(request):
    all_articals=show_pictures_index.objects.all()
    content={'articals':all_articals}
    return render(request,'index.html',content)


def Login_view(request):
    if (request.method=='POST'):
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if(user is None):
            return render(request,'login.html',{"errors":'用户名或者密码错误'})
        else:
            login(request,user)
            return redirect('users:index')
    else:
        return render(request,'login.html')

def Logout_view(request):
    logout(request)
    return redirect('users:index')

def Register_view(request):
    if (request.method=='POST'):
        register_form=forms.SelfDefineUser(request.POST)
        if (register_form.is_valid()):
            register_form.save()
            user=authenticate(username=register_form.cleaned_data['username'],password=register_form.cleaned_data['password1'])
            user.email = register_form.cleaned_data['email']
            models.OrdernaryUser(user=user, nickname=register_form.cleaned_data['昵称']).save()
            login(request,user)
            return redirect('users:index')
    else:
        register_form=forms.SelfDefineUser()
    content={'register_form':register_form}
    return render(request,'register.html',content)

@login_required(login_url='users:login')
def User_center_view(requets):
    content={'user':requets.user}
    return render(requets,'user_center.html',content)
@login_required(login_url='users:login')
def Change_user_message_view(request):
    if request.method=="POST":
        change_message_form=forms.SelfDefineChangeMessage(request.POST,instance=request.user)
        if change_message_form.is_valid():
            change_message_form.save()
            request.user.ordernaryuser.nickname=change_message_form.cleaned_data['昵称']
            request.user.ordernaryuser.save()
            return redirect("users:user_center")
    else:
        change_message_form=forms.SelfDefineChangeMessage(instance=request.user)
    content={"change_message_form":change_message_form,'user':request.user,'ordernaryuser':request.user.ordernaryuser}
    return render(request,'change_message.html',content)

@login_required(login_url='users:login')
def Change_password_view(request):
    if request.method=="POST":
        change_password_form=forms.PasswordChangeForm(data=request.POST,user=request.user)
        if change_password_form.is_valid():
            change_password_form.save()
            return redirect("users:login")
    else:
        change_password_form=forms.PasswordChangeForm(user=request.user)
    content={"change_password_form":change_password_form,'user':request.user,}
    return render(request,'change_password.html',content)

def Artical_test_view(request):
    return render(request,'artical_details.html')

def Pictures_show_details_view(request,id):

    all_message=show_pictures_index.objects.filter(id=id)
    artical=all_message[0].artical
    content={'artical':artical,'id':id}
    return render(request,'artical_details.html',content)