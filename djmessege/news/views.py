from datetime import datetime
from .forms import ArticlesForm
from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import DetailView, UpdateView, DeleteView


class NewDeleteVeiw(DeleteView):
    model = Article
    template_name = 'news/delete.html'
    success_url = '/news'



class NewUpdateVeiw(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewDetailVeiw(DetailView):
    model = Article
    template_name = "news/details_view.html"
    context_object_name = 'article'

def news_home(request):
    news = Article.objects.order_by("-date")
    context = {'news': news}  # Загорніть QuerySet у словник
    return render(request, 'news/news_home.html', context)

def create(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')  # Перенаправлення після збереження
    else:
        form = ArticlesForm()

    context = {
        'form': form
    }
    return render(request, 'news/create.html', context)
