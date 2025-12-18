from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'description', 'author', 'status']
        labels={
            'title':'عنوان پست',
            'description':'توضیحات',
            'author':'نویسنده ',
            'status':'وضعیت پست',
            
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'عنوان پست را وارد کنید'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control custom-input',
                'rows': 5,
                'placeholder': 'توضیحات کامل پست را بنویسید'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control custom-input',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select custom-input'
            }),
        }
