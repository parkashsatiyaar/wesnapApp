from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def home_view(request):
    return HttpResponseRedirect("/posts/")
    # return HttpResponse('Hello world')
