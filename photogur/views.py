
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from photogur.models import * 



def pictures(request): 
    context = { 
        'pictures': Picture.objects.all(), 
        'comments': Comment.objects.all(),
        'comment_2': Comment.objects.get(pk=2) 
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
    search_results = Picture.objects.filter(artist=query)
    # search_results = Picture.objects.filter(artist=query).filter(title=query).filter(url=query)
    context = {'picture': search_results }

    return render(request, 'search.html', context)
