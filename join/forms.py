# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 학번(password1) 필드에 custom-input 클래스 추가
        self.fields['studentId'].widget.attrs.update({
            'class': 'custom-input-studentId',
            'placeholder': '학번',
        })
        # 비밀번호(password2) 필드에 custom-input 클래스 추가
        self.fields['password'].widget.attrs.update({
            'class': 'custom-input-password',
            'placeholder': '비밀번호',
        })
