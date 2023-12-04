from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from .forms import PostForm
from .models import Post, Category

from datetime import datetime,time
from django.utils.dateformat import DateFormat
from django.utils import timezone
from django.http import HttpResponseRedirect

def todo_check(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    print(f'Todo with ID {pk} updated: complete={todo.complete}')
    return redirect('post_list')


def todo_check_no_category(request, pk):
    todo = get_object_or_404(Post, pk=pk, category=None)
    todo.complete = not todo.complete
    todo.save()
    return redirect('category', slug='no_category')


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

        # 이전 날짜
        stored_date_str = self.request.session.get('stored_date')
        # 현재 날짜
        current_date = timezone.now().date()

        print(f'stored_date_str: {stored_date_str}')

        if 'prev' not in self.request.GET and 'next' not in self.request.GET:
            stored_date = current_date
            self.request.session['stored_date'] = stored_date.strftime('%Y-%m-%d')
            stored_date_str = self.request.session.get('stored_date')
        else:
            stored_date = timezone.datetime.strptime(stored_date_str, '%Y-%m-%d').date()

        print(f'stored_date: {stored_date}')

        # 날짜 바꾸기
        if 'prev' in self.request.GET:
            stored_date -= timedelta(days=1)
        elif 'next' in self.request.GET:
            stored_date += timedelta(days=1)

        # 날짜 -> 투두 리스트
        context['post_list_today'] = Post.objects.filter(deadline__date=stored_date)

        # 요일 설정
        dateDict = {0: '월', 1: '화', 2: '수', 3: '목', 4: '금', 5: '토', 6: '일'}

        # 날짜 출력
        today_formatted = DateFormat(stored_date).format('Y.m.d')
        context['today'] = today_formatted + ' (' + dateDict[stored_date.weekday()] + ')'


        # 카테고리
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


def my(request):
    today = datetime.now()
    current_weekday = today.weekday()

    # 현재 날짜에서 현재 요일을 기준으로 월요일을 계산
    monday_of_current_week = today - timedelta(days=current_weekday)

    # 각각의 날짜 변수에 값을 할당
    monday = monday_of_current_week.strftime('%m/%d')
    tuesday = (monday_of_current_week + timedelta(days=1)).strftime('%m/%d')
    wednesday = (monday_of_current_week + timedelta(days=2)).strftime('%m/%d')
    thursday = (monday_of_current_week + timedelta(days=3)).strftime('%m/%d')
    friday = (monday_of_current_week + timedelta(days=4)).strftime('%m/%d')
    saturday = (monday_of_current_week + timedelta(days=5)).strftime('%m/%d')
    sunday = (monday_of_current_week + timedelta(days=6)).strftime('%m/%d')

    # Django의 context에 결과를 저장
    context = {
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        'sunday': sunday,
    }

    return render(
        request,
        'home/my.html',
        context
    )

def get_weekday_number(day):
    # 요일 문자열을 받아 해당하는 숫자를 반환하는 함수
    weekdays = ['월', '화', '수', '목', '금', '토', '일']
    return weekdays.index(day) + 1

def my_view(request, day):
    # 요청된 요일에 해당하는 완료된 과제들을 가져옴
    weekday_number = get_weekday_number(day)
    weekday_posts = Post.objects.filter(complete=True, deadline__week_day=weekday_number)

    return render(request, 'home/my.html', {'weekday_posts': weekday_posts, 'selected_day': day})
