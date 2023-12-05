from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.

def loginpase(request):
    form = LoginForm()
    if request.method == "GET":
        return render(request,'login.html',{'form':form})
    elif request.method == "POST":
        form = LoginForm(request.POST)  
        if form.is_valid():
            enter_id = form.cleaned_data['id']
            enter_pw = form.cleaned_data['password']
            user = authenticate(request, username=enter_id,password=enter_pw)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/main/')
            else:
                error_message = "아이디 또는 비밀번호를 잘못 입력했습니다.입력하신 내용을 다시 확인해주세요."
                return render(request,'login.html',{'form':form,'error':error_message})
        
        
        
        
        
        
def registerpase(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            username_check=form.cleaned_data['id']
            if User.objects.filter(username=username_check).exists():
                name_check = "이미 사용 중인 사용자 아이디입니다."
                return render(request, 'register.html', {'form': form, 'name_check': name_check})
            
            pw = form.cleaned_data['password']
            pw_ck = form.cleaned_data['passwordcheck']
            if pw == pw_ck:
                
                user = User.objects.create_user(
                    username=username_check,
                    email=form.cleaned_data['email'],
                    password=pw
                )
                login(request, user)
                return render(request, 'main.html')
            
            else:
                form = RegisterForm()
                error_check = "비밀번호가 일치하지 않습니다."
                return render(request, 'register.html', {'form': form, 'error_check': error_check})
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})