from django.shortcuts import render,redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth import logout
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def mainpase(request):
    if request.user.is_authenticated:
        now_username=request.user.username
        return render(request, 'main.html',{'name':now_username})
    else:
        return render(request, 'main.html')
    

@xframe_options_exempt
def mypasesmall_view(request):
    return render(request, 'mypasesmall.html')
    
    
@xframe_options_exempt
def logout_funtion(request):
    logout(request)
    main_url = reverse('main')
    return HttpResponse(f"<script>window.top.location.href = '{main_url}';</script>")