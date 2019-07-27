
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from photogur.models import * 


def pictures(request): 
    context = { 'pictures': Picture.objects.all(), 
    'comments': Comment.objects.all(),
    'comment_2': Comment.objects.get(pk=2)  }
    response = render(request, 'pictures.html', context)
    return HttpResponse(response) 

def root(request): 
    return HttpResponseRedirect('pictures/')
