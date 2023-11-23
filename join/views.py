from django.shortcuts import render

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

