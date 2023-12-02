from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            studentId = form.get_user()
            login(request, studentId)
            return redirect('join:login')  # home은 프로젝트에 따라 수정해야 할 수 있습니다.
    else:
        form = AuthenticationForm()
        context = {'form': form}

    return render(
        request,
        'join/login.html',
        context
    )

def logout(request):
    auth_logout(request)
    return redirect('join:login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # home은 프로젝트에 따라 수정해야 할 수 있습니다.
    else:
        form = UserCreationForm()
    return render(
        request,
        'join/signup.html',
    )

