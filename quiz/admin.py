from django.contrib import admin

from .models import Category, Test, Question, Answer, Article, Tag

admin.site.register(Category)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Article)
admin.site.register(Tag)