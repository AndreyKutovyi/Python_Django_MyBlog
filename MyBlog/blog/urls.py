from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','blog.views.home', name='home'),
    url(r'^news/(?P<news_id>[0-9]+)/$', 'blog.views.show_news', name='news_posts'),
    url(r'^teachers_of_kaf/$', 'blog.views.teachers_of_kaf', name='teachers_of_kaf'),
    url(r'^literature/$', 'blog.views.literature', name='literature'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', 'blog.views.show_article', name='article'),
    url(r'^timetable/$', 'blog.views.timetable', name='timetable'),
    url(r'^subjects/$', 'blog.views.subjects', name='subjects'),
     url(r'^subjects/(?P<subject_id>[0-9]+)/$', 'blog.views.show_subject', name='subject')
]
