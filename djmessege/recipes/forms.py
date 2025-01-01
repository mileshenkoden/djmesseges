from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateInput
from django import forms
from .models import Rating

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


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

    rating = forms.ChoiceField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)],
                               widget=forms.RadioSelect)

