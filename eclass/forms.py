from django import forms
from .models import Assignment, Quiz

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'content', 'due_date']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '제목 작성',
                }),
            'content': forms.Textarea(
                attrs={
                    'placeholder': '내용 작성'
                }),
            'due_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                }),
        }

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'due_date', 'questions']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '제목 작성',
                }),
            'questions': forms.Textarea(
                attrs={
                    'placeholder': '문제 출시'
                }),
            'due_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                }),
        }