from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/start.html'
    )


def about_us(request):
    return render(
        request,
        'single_pages/about_us.html'
    )