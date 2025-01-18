from django.contrib import admin
from .models import Article, Step, Rating

class StepInline(admin.TabularInline):
    model = Step
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [StepInline]

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'rating')
