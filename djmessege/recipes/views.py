from datetime import datetime
from urllib import request
from .forms import ArticlesForm, StepFormSet
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.core.files.storage import default_storage
from .models import Article, Step
from django.forms.models import inlineformset_factory
from django.contrib import messages



class NewDeleteView(DeleteView):


    model = Article
    template_name = 'recipes/delete.html'
    success_url = '/recipes'


class NewUpdateView(UpdateView):
    model = Article
    template_name = 'recipes/create.html'
    form_class = ArticlesForm


class NewDetailView(DetailView):
    model = Article
    template_name = "recipes/details_view.html"
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def recipes_home(request):
    recipes = Article.objects.all()  # Отримуємо всі статті з бази даних
    return render(request, 'recipes/recipes_home.html', {'recipes': recipes})




def create(request):
    StepFormSet = inlineformset_factory(
        Article,
        Step,
        fields=['text', 'image'],  # Поля для тексту та зображень
        extra=1,
        can_delete=True
    )

    if request.method == "POST":
        # Отримуємо дані з форми для статті
        form = ArticlesForm(request.POST, request.FILES)
        formset = StepFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            # Зберігаємо статтю
            article = form.save()

            # Обробляємо кроки інструкцій
            steps = formset.save(commit=False)
            for step in steps:
                step.article = article  # Прив'язуємо крок до статті
                step.save()  # Зберігаємо крок разом із фото

            messages.success(request, "Рецепт успішно збережено!")
            return redirect('recipes_home')
        else:
            messages.error(request, "Будь ласка, перевірте форму на наявність помилок.")
    else:
        form = ArticlesForm()
        formset = StepFormSet()

    return render(request, 'recipes/create.html', {'form': form, 'formset': formset})

