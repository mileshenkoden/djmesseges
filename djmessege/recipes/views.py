from datetime import datetime
from .forms import ArticlesForm
from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import DetailView, UpdateView, DeleteView
from django.core.files.storage import default_storage

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



import json

def create(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            # Перетворення рядка інструкцій у список
            article.instructions = json.loads(request.POST.get('instructions'))
            article.save()
            return redirect('recipes_home')
    else:
        form = ArticlesForm()

    return render(request, 'recipes/create.html', {'form': form})
