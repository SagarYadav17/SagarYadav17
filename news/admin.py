from django.contrib import admin
from news.models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "source")
    search_fields = ("title",)
    list_filter = ("category", "source")


class SourceAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Category, CategoryAdmin)
