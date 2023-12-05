from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from . import models
from .forms import PostForm
from .models import Post, Category
from eclass.models import Assignment, Quiz

from datetime import datetime, time, timedelta
from django.utils.dateformat import DateFormat
from django.utils import timezone
from django.http import HttpResponseRedirect



def todo_check(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    todo.complete = not todo.complete
    todo.save()

    referer = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(referer)


def todo_check_category(request, pk, slug):
    category = get_object_or_404(Category, slug=slug)
    todo = get_object_or_404(Post, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect('home:category', slug=category.slug)


def todo_check_no_category(request, pk):
    todo = get_object_or_404(Post, pk=pk, category=None)
    todo.complete = not todo.complete
    todo.save()
    return redirect('home:category', slug='no_category')


def todo_check2(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    todo.complete = not todo.complete
    todo.save()
    return redirect(f'../../../home/check_details_{pk}/')


def category_page(request, slug):
    if slug == 'no_category':
        category = 'e-class'
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


def createEclassPost(title, content, deadline, activity):
    return Post.objects.create(
        title=str('['+activity.lecture.name+'] ')+title,
        content=content,
        deadline=deadline,
        complete=False,
        category=None,
    )


class PostList(ListView):
    model = Post
    ordering = '-pk'

    assignments = Assignment.objects.all()
    quizzes = Quiz.objects.all()

    for assignment in assignments:
        if not Post.objects.filter(title=str('['+assignment.activity.lecture.name+'] ')+assignment.title, content=assignment.content,
                                   deadline=assignment.due_date).exists():
            createEclassPost(assignment.title, assignment.content, assignment.due_date,assignment.activity)
    for quiz in quizzes:
        if not Post.objects.filter(title=str('['+quiz.activity.lecture.name+'] ')+quiz.title, content=quiz.questions, deadline=quiz.due_date).exists():
            createEclassPost(quiz.title, quiz.questions, quiz.due_date, quiz.activity)

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

        # 변경 날짜 저장
        self.request.session['stored_date'] = stored_date.strftime('%Y-%m-%d')

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
    if request.method == "POST":  # 글을 수정사항을 입력하고 제출을 눌렀을 때
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.deadline = form.cleaned_data['deadline']
            post.category = form.cleaned_data['category']
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


def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('../../home/')


def my(request):
    today = timezone.now().date()
    current_weekday = today.weekday()
    # 현재 날짜에서 현재 요일을 기준으로 월요일을 계산
    monday_of_current_week = today - timedelta(days=current_weekday)

    # 각각의 날짜 변수에 값을 할당
    monday = (monday_of_current_week).strftime('%Y-%m-%d')
    tuesday = (monday_of_current_week + timedelta(days=1)).strftime('%Y-%m-%d')
    wednesday = (monday_of_current_week + timedelta(days=2)).strftime('%Y-%m-%d')
    thursday = (monday_of_current_week + timedelta(days=3)).strftime('%Y-%m-%d')
    friday = (monday_of_current_week + timedelta(days=4)).strftime('%Y-%m-%d')
    saturday = (monday_of_current_week + timedelta(days=5)).strftime('%Y-%m-%d')
    sunday = (monday_of_current_week + timedelta(days=6)).strftime('%Y-%m-%d')

    monday_date = timezone.make_aware(timezone.datetime.strptime(monday, '%Y-%m-%d')).date()
    tuesday_date = timezone.make_aware(timezone.datetime.strptime(tuesday, '%Y-%m-%d')).date()
    wednesday_date = timezone.make_aware(timezone.datetime.strptime(wednesday, '%Y-%m-%d')).date()
    thursday_date = timezone.make_aware(timezone.datetime.strptime(thursday, '%Y-%m-%d')).date()
    friday_date = timezone.make_aware(timezone.datetime.strptime(tuesday, '%Y-%m-%d')).date()
    saturday_date = timezone.make_aware(timezone.datetime.strptime(saturday, '%Y-%m-%d')).date()
    sunday_date = timezone.make_aware(timezone.datetime.strptime(sunday, '%Y-%m-%d')).date()

    print(f'Monday Date: {monday_date}')
    monday_posts = Post.objects.filter(deadline__date=monday_date)
    print(f'Monday Posts: {monday_posts}')

    print(f'Tuesday Date: {tuesday_date}')
    tuesday_posts= Post.objects.filter(deadline__date=tuesday_date)
    print(f'Tuesday Posts: {tuesday_posts}')

    print(f'Wednesday Date: {wednesday_date}')
    wednesday_posts = Post.objects.filter(deadline__date=wednesday_date)
    print(f'Wednesday Posts: {wednesday_posts}')

    print(f'Thursday Date: {thursday_date}')
    thursday_posts = Post.objects.filter(deadline__date=thursday_date)
    print(f'Thursday Posts: {thursday_posts}')

    print(f'Friday Date: {friday_date}')
    friday_posts = Post.objects.filter(deadline__date=friday_date)
    print(f'Friday Posts: {friday_posts}')

    print(f'Saturday Date: {saturday_date}')
    saturday_posts = Post.objects.filter(deadline__date=saturday_date)
    print(f'Saturday Posts: {saturday_posts}')

    print(f'Sunday Date: {sunday_date}')
    sunday_posts = Post.objects.filter(deadline__date=sunday_date)
    print(f'Sunday Posts: {sunday_posts}')

    # Django의 context에 결과를 저장
    context = {
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        'sunday': sunday,

        'monday_posts': monday_posts,
        'tuesday_posts': tuesday_posts,
        'wednesday_posts': wednesday_posts,
        'thursday_posts': thursday_posts,
        'friday_posts': friday_posts,
        'saturday_posts': saturday_posts,
        'sunday_posts': sunday_posts,
    }

    return render(
        request,
        'home/my.html',
        context,
    )

#
# def get_weekday_number(day):
#     weekdays = ['월', '화', '수', '목', '금', '토', '일']
#     return weekdays.index(day) + 1
#
# def my_view(request, day):
#     weekday_number = get_weekday_number(day)
#     weekday_posts = Post.objects.filter(complete=True, deadline__week_day=weekday_number)
#
#     return render(request, 'home/my.html', {'weekday_posts': weekday_posts, 'selected_day': day})
#
