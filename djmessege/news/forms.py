from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "intro", "full_text", "date"]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Назва статті"
            }),
            "intro": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть короткий вступ"
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введіть текст статті"
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
