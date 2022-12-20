from django.shortcuts import render
from django.http import HttpResponse


def hello_world_func(request):
    match request.method:
        case 'GET':
            return HttpResponse('Hello, World!')
