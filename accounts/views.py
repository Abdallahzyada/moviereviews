from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import UserCreateForm
# Create your views here.

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form' : UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form':UserCreateForm,
                                                              "error":'User Already TAKEN, choose new username.'})
        else:
            return render(request, 'signupaccount.html', {'form':UserCreateForm,
                                                          'error':'Password Do NOT match'})
            
            
def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request,
                            username = request.POST['username'],
                            password = request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form':AuthenticationForm,
                                                         'error':'username and password DO NOT match.'})
        else:
            login(request)
            redirect('home')

@login_required            
def logoutaccount(request):
    logout(request)
    return redirect('home')
            