# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     account = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)
#     name = models.CharField(max_length=150, unique=True)
#     department = models.CharField(max_length=150)
#     phone = models.CharField(max_length=150)
#     email = models.EmailField(max_length=254)
#     active_date = models.IntegerField(default=180)
#     fail_total = models.IntegerField()
#     lock_time = models.DateTimeField()
#     create_time = models.DateTimeField()
#     create_by = models.CharField(max_length=150)
#     update_time = models.DateTimeField()
#     update_by = models.CharField(max_length=150)
#     pwd_updatetime = models.DateTimeField()

class Book(models.Model):
    book_name = models.CharField(max_length=150)
    add_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.book_name

class Student(models.Model):#学生模板
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    learn = models.CharField(max_length=150)
    def __unicode__(self):
        return self.name

class Teacher(models.Model):#老师模板
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    teach = models.CharField(max_length=150)
    student = models.ManyToManyField( Student,through = "OneClass")
    def __unicode__(self):
        return self.name

class OneClass(models.Model):#班级模板
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name


# 日志
class Log(models.Model):
    id = models.IntegerField(primary_key=True)
    opera_info = models.CharField(max_length=150)
    opera_type = models.CharField(max_length=150)
    server_ip = models.CharField(max_length=150)
    menu_name = models.CharField(max_length=150)
    result = models.CharField(max_length=150)
    session_id = models.CharField(max_length=150)
    opera_by = models.CharField(max_length=150)
    opera_time = models.CharField(max_length=150)

#登陆日志
class Login_log(models.Model):
    account = models.CharField(max_length=150)
    time = models.DateTimeField()
    ip = models.CharField(max_length=150)
    status = models.IntegerField()
