from django.contrib import admin

# Register your models here.
from blog.models import Article, Subject, Teacher,News

admin.site.register(Article)
admin.site.register(Subject)
admin.site.register(Teacher)

admin.site.register(News)