
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from photogur.models import * 
from django.contrib.postgres.search import SearchVector
from django.shortcuts import redirect


def pictures(request): 
    context = { 
        'pictures': Picture.objects.all(), 
        'comments': Comment.objects.all()
    }
    response = render(request, 'pictures.html', context)
    return HttpResponse(response) 

def root(request): 
    return HttpResponseRedirect('pictures/')


def picture_show(request, id): 
    picture = Picture.objects.get(pk=id) 
    context = {
        'picture': picture
    }
    return render(request, 'picture.html', context) 

    
def picture_search(request): 
    query = request.GET['query']
    search_results = Picture.objects.filter(title__contains=query) or Picture.objects.filter(artist__contains=query) or Picture.objects.filter(url__contains=query)
    context = {'picture': search_results, 'query': query}

    return render(request, 'search.html', context)

def create_comment(request): 

    params = request.POST
    picture_id = params['picture']
    picture = Picture.objects.get(pk=picture_id) 

    comment = Comment() 
    comment.name = params['name']
    comment.message = params['message']
    comment.picture = picture
    comment.save()
   
    return HttpResponseRedirect(f'/pictures/{picture_id}')

def delete(request, id): 
    comment = Comment.objects.get(pk=id) 
    comment.delete() 
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



    
