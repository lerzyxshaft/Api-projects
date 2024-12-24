from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post name'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons name'
            }),
            'Date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'publication date'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Post text'
            })

        }