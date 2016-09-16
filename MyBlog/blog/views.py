from django.shortcuts import render, get_object_or_404,HttpResponse

# Create your views here.
from blog.models import Article
from blog.models import Teacher
from blog.models import Subject
from blog.models import News


def home(request):
    articles = News.objects.all()
    context = {
        'news': articles
    }
    return render(request, 'blog/home.html', context)


def teachers_of_kaf(request):
    teachers=Teacher.objects.all()
    subjects=Subject.objects.all()
    context={
        'teachers':teachers,
        'subjects':subjects,
    }
    return render(request, 'blog/teachers_of_kaf.html', context)


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article': article})

def show_news(request, news_id):
    article = get_object_or_404(News, id=news_id)
    return render(request, 'blog/particular_news.html', {'news': article})

def literature(request):
    return render(request, 'blog/literature.html')


def timetable(request):
    return render(request, 'blog/timetable.html')

def subjects(request):
    subjects_1=Subject.objects.all()
    teachers = Teacher.objects.all()
    context={
        'subjects':subjects_1,
        'teachers':teachers
    }
    return render(request, 'blog/subjects.html', context)

def show_subject(request, subject_id):
    #subject = get_object_or_404(Subject, id=subject_id)
    article = Article.objects.filter(name_of_subject=subject_id)
    context ={
       # "subject": subject,
        "articles": article,

    }
    return render(request, 'blog/subject.html', context)
