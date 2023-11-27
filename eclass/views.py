from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import Lecture, Activity, Quiz, Assignment
from .forms import AssignmentForm, QuizForm

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

def assignment_creation(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.activity = activity
            assignment.save()
            return redirect('lecture_list')
    else:
        form = AssignmentForm()

    return render(request, 'assignment_creation.html', {'form': form})

def quiz_creation(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.activity = activity
            quiz.save()
            return redirect('lecture_list')
    else:
        form = QuizForm()

    return render(request, 'quiz_creation.html', {'form': form})