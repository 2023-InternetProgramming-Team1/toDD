from django.shortcuts import render, redirect
from .models import Lecture, Activity, Quiz, Assignment

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'eclass/lecture_list.html', {'lectures': lectures})

def lecture_detail(request, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    activities = Activity.objects.filter(lecture=lecture)
    return render(request, 'eclass/lecture_detail.html', {'lecture': lecture, 'activities': activities})

def activity_detail(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    return render(request, 'eclass/activity_detail.html', {'activity': activity})

def quiz_create(request, activity_id):
    if request.method == 'POST':
        # 퀴즈 생성 로직
        return redirect('activity_detail', activity_id=activity_id)
    return render(request, 'eclass/quiz_create.html')

def assignment_create(request, activity_id):
    if request.method == 'POST':
        # 과제 생성 로직
        return redirect('activity_detail', activity_id=activity_id)
    return render(request, 'eclass/assignment_create.html')
