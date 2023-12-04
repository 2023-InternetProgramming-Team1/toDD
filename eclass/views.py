from django.shortcuts import render, redirect, get_object_or_404
from .models import Lecture, Activity, Assignment, Quiz
from .forms import AssignmentForm, QuizForm

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture_list.html', {'lectures': lectures})

def lecture_detail(request, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    activities = Activity.objects.filter(lecture=lecture)
    return render(request, 'lecture_detail.html', {'lecture': lecture, 'activities': activities})

def activity_detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'activity_detail.html', {'activity': activity})

def assignment_creation(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = Assignment()
            assignment.title = form.cleaned_data['title']
            assignment.content = form.cleaned_data['content']
            assignment.due_date = form.cleaned_data['due_date']
            assignment.activity = activity
            assignment.save()
            return redirect('lecture_detail', lecture_id=activity.lecture.id)
    else:
        form = AssignmentForm()

    return render(request, 'assignment_creation.html', {'form': form, 'activity': activity})


def quiz_creation(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = Quiz()
            quiz.title = form.cleaned_data['title']
            quiz.questions = form.cleaned_data['questions']
            quiz.due_date = form.cleaned_data['due_date']
            quiz.activity = activity
            quiz.save()
            return redirect('lecture_detail', lecture_id=activity.lecture.id)
    else:
        form = QuizForm()

    return render(request, 'quiz_creation.html', {'form': form, 'activity':activity})