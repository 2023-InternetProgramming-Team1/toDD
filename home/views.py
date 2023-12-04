from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from .forms import PostForm
from .models import Post, Category

from datetime import datetime,time
from django.utils.dateformat import DateFormat

def todo_check(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    print(f'Todo with ID {pk} updated: complete={todo.complete}')
    return redirect('post_list')

def todo_check_category(request, pk, slug):
    category = get_object_or_404(Category, slug=slug)
    todo = get_object_or_404(Post, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect('category', slug=category.slug)

def todo_check2(request, pk):

    todo = get_object_or_404(Post, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    print(f'Todo with ID {pk} updated: complete={todo.complete}')
    return redirect(f'../../../home/check_details_{pk}/')

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = get_object_or_404(Category, slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'home/category_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_categories_post_count': Post.objects.filter(category=None).count(),
            'category': category,
            'no_category_slug': 'no_category',
        }
    )

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        today = datetime.now()
        dateDict = {0: '월', 1: '화', 2: '수', 3: '목', 4: '금', 5: '토', 6: '일'}
        context['today'] = DateFormat(today).format('Y.m.d') + ' (' + dateDict[today.weekday()] + ')'
        return context

class CategoryList(ListView):
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post


def postCreate(request):
    if request.method == "POST":  # 데이터를 저장할 때
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.deadline = form.cleaned_data['deadline']
            post.category = form.cleaned_data['category']
            post.save()
            return redirect(post)
    else:  # 입력 양식을 보여줄 때
        form = PostForm()
    return render(request, 'home/post_form.html', {
        'form': form
    })


def postEdit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST": # 글을 수정사항을 입력하고 제출을 눌렀을 때
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.deadline = form.cleaned_data['deadline']
            post.category = form.cleaned_data['category']
            post.save()
        return redirect(post)
    else: # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
        form = PostForm(instance=post)
        context = {
            'form': form,
            'writing': True,
            'now': 'edit',
        }
    return render(request, 'home/edit_post_form.html', context)


def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('../../home/')





def popup(request):
    post_content = Post.objects.all()
    return render(request, 'home/popup.html', {'post_content': post_content})

