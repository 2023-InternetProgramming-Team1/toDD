from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import PostForm
from .models import Post, Category
from django.http import JsonResponse


def todo_check(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    print(f'Todo with ID {pk} updated: complete={todo.complete}')
    return redirect('post_list')



def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'home/category_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_categories_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
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
    if request.method == "POST":  # 데이터를 저장해야할때
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.deadline = form.cleaned_data['deadline']
            post.save()
            return redirect(post)
    else:  # 입력 양식을 보여줘야 할때
        form = PostForm()
    return render(request, 'home/post_form.html', {
        'form': form
    })


def postEdit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":  # 글을 수정사항을 입력하고 제출을 눌렀을 때
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.deadline = form.cleaned_data['deadline']
            post.save()
        return redirect(post)
    else:  # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
        form = PostForm(instance=post)
        context = {
            'form': form,
            'writing': True,
            'now': 'edit',
        }
    return render(request, 'home/edit_post_form.html', context)
