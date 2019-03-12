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

# 合同对象
class Contract(models.Model):
    name = models.CharField(max_length=150, unique=True)
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=150)
    hash_number = models.CharField(max_length=150)
    opinion = models.TextField()
    money = models.FloatField()
    type = models.CharField(max_length=150)
    summary = models.CharField(max_length=150)
    dept = models.CharField(max_length=150)
    verify = models.BooleanField()
    responsible_person = models.CharField(max_length=150)
    supplier_id = models.IntegerField()
    status = models.IntegerField()

# 电子合同存放地址表
class Contract_Location(models.Model):
    id = models.IntegerField(primary_key=True)
    contract_id = models.IntegerField()
    location = models.FilePathField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=150)
    status = models.IntegerField()

# 扫描件信息表
class Scan_Info(models.Model):
    id = models.IntegerField()
    contract_id = models.IntegerField()
    name = models.CharField(max_length=150)
    location = models.FilePathField()
    status = models.IntegerField()
    verify_result = models.IntegerField()
    review_result = models.IntegerField()
    review_by = models.CharField(max_length=150)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=150)
    update_time = models.DateTimeField()
    update_by = models.CharField(max_length=150)
    review_remark = models.TextField()

# 供应商表
class Supplier(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=150, unique=True)
    manager = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    remark = models.T