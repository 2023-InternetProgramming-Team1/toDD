from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.shortcuts import redirect


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'


def remove(request, id):
    remove_alarm = Post.objects.get(id= id)
    remove_alarm.delete()

    return redirect('alarm')


def popup(request):
    return render(
        request,
        'alarm/popup.html'
    )