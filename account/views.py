from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import SignupForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm


# Create your views here.

def index(request):
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
            
    return render(request, 'registration/login.html',{'form':form})
    

def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')  # 프로필 페이지로 리다이렉트
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'profile_update.html', {'form': form})

class MyPasswordChangeView(PasswordChangeView):
    success_url=reverse_lazy('account:profile')
    template_name='account/password_change_form.html'
    
    def form_valid(self, form):
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)
    