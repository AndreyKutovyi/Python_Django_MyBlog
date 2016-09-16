# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import PIL
from PIL import Image

# Create your models here.
SHORT_TEXT_LEN = 1000

#------------------------------------------
class Subject(models.Model):
    title = models.CharField(u'Название предмета',max_length=200)
    course=models.IntegerField(u'Курс на котором читаеться предмет',null=True)
   # numbers_of_articles=models.ManyToManyField(Article)

    def __unicode__(self):
        return self.title

#------------------------------------------
class Article(models.Model):
    title = models.CharField(u'Название',max_length=200)
    text = models.TextField(u'Текст статьи',null=True)
    user = models.ForeignKey(User, null=True)
    name_of_subject=models.ForeignKey(Subject,null=True)

    def __unicode__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text
#------------------------------------------

class News(models.Model):
    title = models.CharField(u'Название',max_length=200)
    text = models.TextField(u'Текст статьи',null=True)
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text
#------------------------------------------

class Teacher(models.Model):
    surname = models.CharField(u'фамилия',max_length=50)
    name = models.CharField(u'Имя',max_length=50)
    midle_name = models.CharField(u'Отчество',max_length=50)
    subjects = models.ForeignKey(Subject,null=True)
    e_mail = models.EmailField(null=True)
    image=models.ImageField(upload_to='images/',verbose_name=u'Ваше фото', help_text='150x150px',null=True)

    def __unicode__(self):
        return self.surname + " "+self.name+" "+self.midle_name
