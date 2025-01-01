from venv import create

from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_home, name='recipes_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.NewUpdateVeiw.as_view(), name='recipes-update'),
    path('<int:pk>', views.NewDetailVeiw.as_view(), name='recipes-detail'),
    path('<int:pk>/delete', views.NewDeleteVeiw.as_view(), name='recipes-delete'),
path('<int:article_id>/rate/', views.rate_article, name='rate_article'),
]



