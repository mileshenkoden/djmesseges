from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateInput
from django import forms
from .models import Rating
from django.forms.models import inlineformset_factory
from .models import Step
from django.core.exceptions import ValidationError
import json


StepFormSet = inlineformset_factory(
    Article,
    Step,
    fields=['text', 'image'],
    extra=1,
    can_delete=True,
)


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'photo', 'description', 'ingredients', 'instructions', 'notes']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва рецепту'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Короткий опис'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Інгредієнти'}),
            'instructions': forms.HiddenInput(),  # Інструкції додаються через JavaScript
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Примітки (необов’язково)'}),
        }

    def clean_instructions(self):
        instructions = self.cleaned_data.get('instructions')  # Отримуємо дані з форми

        # Якщо значення — список, пропускаємо перетворення
        if isinstance(instructions, list):
            parsed_instructions = instructions
        else:
            # Якщо це строка, перетворюємо її на список
            try:
                parsed_instructions = json.loads(instructions)
            except json.JSONDecodeError:
                raise ValidationError('Невірний формат JSON для інструкцій.')

        # Перевіряємо, чи це справді список
        if not isinstance(parsed_instructions, list):
            raise ValidationError('Інструкції мають бути списком.')

        # Валідуємо кожен крок
        for step in parsed_instructions:
            if 'text' not in step or not step['text']:
                raise ValidationError('Кожен крок повинен мати опис.')
            if 'image' not in step:  # Переконаємося, що ключ `image` є в кожному кроці
                raise ValidationError('У кожному кроці повинно бути поле "image".')

        return parsed_instructions


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

    rating = forms.ChoiceField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)],
                               widget=forms.RadioSelect)

