from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateInput
from django import forms
from .models import Rating

class ArticlesForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'photo', 'description', 'ingredients', 'instructions', 'notes']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва рецепту'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Короткий опис'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Інгредієнти'}),
            'instructions': forms.HiddenInput(),  # Інструкції будуть динамічно додаватися через JavaScript
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Примітки (необов’язково)'}),
        }
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

    rating = forms.ChoiceField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)],
                               widget=forms.RadioSelect)

