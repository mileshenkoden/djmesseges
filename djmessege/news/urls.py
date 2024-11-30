from venv import create

from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.NewUpdateVeiw.as_view(), name='news-update'),
    path('<int:pk>', views.NewDetailVeiw.as_view(), name='news-detail'),
    path('<int:pk>/delete', views.NewDeleteVeiw.as_view(), name='news-delete'),
]



