from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'deadline', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'background-color: #FFFFF4; max-length: 30;',
                    'placeholder': '제목 작성',
                }),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control border-0',
                    'cols': 70,
                    'rows': 8,
                    'style': 'background-color: #FFF7D3;',
                    'placeholder': '내용 작성',
                }),
            'deadline': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control border-0',
                    'style': 'background-color: #FFEC9D;',
                }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].widget.attrs.update({
            'class': 'form-control border-0',
            'style': 'background-color: #FFEC9D;',
        })

