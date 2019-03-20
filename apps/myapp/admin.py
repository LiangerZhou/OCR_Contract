# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.contrib import admin
import xadmin
# from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Book

xadmin.site.register(Book)