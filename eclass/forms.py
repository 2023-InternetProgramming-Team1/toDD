from django import forms
from .models import Assignment, Quiz

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'due_date', 'content']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'due_date', 'questions']
