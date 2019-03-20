# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json

from myapp.models import Book,Contract

# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['bookList'] = json.loads(serializers.serialize("json",books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    
    return JsonResponse(response)


    # 合同管理

    ## 合同查询请求 get
@require_http_methods(["GET"]) #@require_GET()
def show_contracts(request):
    response = {}
    try:
        contracts = Contract.objects.filter()
        response['contractList'] = json.loads(serializers.serialize("json",contracts))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        
    ## 合同验真请求 post

    ## 验真快照查询请求 get

    ## 供应商查询请求 get

    ## 合同名称校验请求 post

    ## 合同上传 post

    ## 扫描件上传 post

    ## 扫描件上传进度查询 get

    ## 提交对比请求 post

    ## 差异概要表查询 get   mongodb操作

    ## 文本对比结果查询 get