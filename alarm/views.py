from django.shortcuts import *
from django.views.generic import ListView
from .models import Post
from django.views.decorators.http import require_POST


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/alarm/')
    return render(request, 'alarm/alarm_remove.html', {'Post': post})

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

def popup(request):
    return render(
        request,
        'alarm/popup.html'
    )

