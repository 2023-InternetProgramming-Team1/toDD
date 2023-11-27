from django.shortcuts import render

# Create your views here.
def login(request):
    return render(
        request,
        'join/login.html',
    )

def account(request):
    return render(
        request,
        'join/account.html',
    )

def mypage(request):
    return render(
        request,
        'join/mypage.html',
    )

