from datetime import datetime
from .forms import ArticlesForm
from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


class NewDeleteVeiw(DeleteView):
    model = Article
    template_name = 'recipes/delete.html'
    success_url = '/recipes'



class NewUpdateVeiw(UpdateView):
    model = Article
    template_name = 'recipes/create.html'
    form_class = ArticlesForm

class NewDetailVeiw(DetailView):
    model = Article
    template_name = "recipes/details_view.html"
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['full_stars'] = range(int(article.average_rating))
        context['empty_stars'] = range(5 - int(article.average_rating))
        return context


@login_required
def rate_article(request, article_id):
    if request.method == "POST":
        try:
            article = get_object_or_404(Article, pk=article_id)
            rating_value = int(request.POST.get('rating'))
            if not (1 <= rating_value <= 5):
                return HttpResponseBadRequest("Рейтинг має бути в межах 1-5.")

            # Перевіряємо, чи вже існує рейтинг від цього користувача
            rating, created = Rating.objects.get_or_create(user=request.user, article=article)
            rating.rating = rating_value
            rating.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except (ValueError, Article.DoesNotExist):
            return HttpResponseBadRequest("Некоректні дані.")
    return HttpResponseBadRequest("Метод не підтримується.")
def recipes_home(request):
    recipes = Article.objects.order_by("-date")
    for recipe in recipes:
        recipe.full_stars = range(int(recipe.avg_rating()))  # Виклик методу з дужками
        recipe.empty_stars = range(5 - int(recipe.avg_rating()))  # Виклик методу з дужками
    context = {'recipes': recipes}
    return render(request, 'recipes/recipes_home.html', context)



def create(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes_home')  # Перенаправлення після збереження
    else:
        form = ArticlesForm()

    context = {
        'form': form
    }
    return render(request, 'recipes/create.html', context)
