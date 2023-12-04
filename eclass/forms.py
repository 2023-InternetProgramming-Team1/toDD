from django import forms
from .models import Assignment, Quiz

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'content', 'due_date']
        labels = {
            'title': '제목',
            'content': '내용',
            'due_date': '마감 일시',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '제목 작성',
                }),
            'content': forms.Textarea(
                attrs={
                    'class': 'custom-textarea',
                    'placeholder': '내용 작성'
                }),
            'due_date': forms.DateTimeInput(
                attrs={
                    'class': 'custom-due-date',
                    'type': 'datetime-local',
                }),
        }

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'due_date', 'questions']
        labels = {
            'title': '제목',
            'questions': '문제',
            'due_date': '마감 일시',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '제목 작성',
                }),
            'questions': forms.Textarea(
                attrs={
                    'class': 'custom-textarea',
                    'placeholder': '문제 출시'
                }),
            'due_date': forms.DateTimeInput(
                attrs={
                    'class': 'custom-due-date',
                    'type': 'datetime-local',
                }),
        }