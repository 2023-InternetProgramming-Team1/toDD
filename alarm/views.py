from django.shortcuts import *
from .models import CheckThis, Updated
from django.views.decorators.http import require_POST


def alarm(request):
    check_this_content = CheckThis.objects.all()
    updated_content = Updated.objects.all()
    return render(
        request,
        'alarm/alarm_list.html',
        {'check_this_content': check_this_content, 'updated_content':updated_content}
    )


def remove_check_this(request, pk):
    post = CheckThis.objects.get(pk=pk)
    check_this_content = CheckThis.objects.all()
    updated_content = Updated.objects.all()
    if request.method == 'POST':
        post.delete()
        return redirect('/alarm/')
    return render(
        request,
        'alarm/check_this_remove.html',
        {'Post': post, 'check_this_content': check_this_content, 'updated_content':updated_content}
    )


def remove_assignment(request, pk):
    assignment = Updated.objects.get(pk=pk)
    check_this_content = CheckThis.objects.all()
    updated_content = Updated.objects.all()
    if request.method == 'POST':
        assignment.delete()
        return redirect('/alarm/')
    return render(
        request,
        'alarm/assignment_remove.html',
        {'Assignment': assignment, 'check_this_content': check_this_content, 'updated_content':updated_content}
    )


def remove_quiz(request, pk):
    quiz = Updated.objects.get(pk=pk)
    check_this_content = CheckThis.objects.all()
    updated_content = Updated.objects.all()
    if request.method == 'POST':
        quiz.delete()
        return redirect('/alarm/')
    return render(
        request,
        'alarm/quiz_remove.html',
        {'Quiz': quiz, 'check_this_content': check_this_content, 'updated_content':updated_content}
    )

