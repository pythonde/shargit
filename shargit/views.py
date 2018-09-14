#coding=utf-8

from django.http import HttpResponse

def index_view(request):
    return HttpResponse('hello git')


def stu2_view(request):
    return HttpResponse('stu2')