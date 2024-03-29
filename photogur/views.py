
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect, get_object_or_404
from photogur.models import * 
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse



def root(request): 
    return HttpResponseRedirect('pictures/')

def pictures(request):
    if request.user.is_authenticated: 
        context = { 
            'pictures': Picture.objects.all(), 
            'comments': Comment.objects.all()
        }
        response = render(request, 'pictures.html', context)
        return HttpResponse(response) 
    else: 
        return redirect('/accounts/signup')

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/pictures')

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/pictures')


@login_required
def picture_show(request, id): 
    picture = get_object_or_404(Picture, pk=id) 
    context = {'picture': picture}
    return render(request, 'picture.html', context) 


def picture_search(request): 
    query = request.GET['query']
    search_results = Picture.objects.filter(title__contains=query) or Picture.objects.filter(artist__contains=query) or Picture.objects.filter(url__contains=query)
    context = {'picture': search_results, 'query': query}

    return render(request, 'search.html', context)

@login_required
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

@login_required
def delete(request, id): 
    comment = Comment.objects.get(pk=id) 
    comment.delete() 
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def signup(request): 
    form = UserCreationForm() 
    context = { 'form': form }
    return render(request, 'registration/signup.html', context) 


def signup_create(request): 
    form = UserCreationForm(request.POST) 
    if form.is_valid(): 
        new_user = form.save() 
        login(request, new_user) 
        return redirect('/')

    else: 
        context = { 'form': form }
        return render(request, 'registration/signup.html', context) 

@login_required
def edit_picture(request, id): 
    picture = get_object_or_404(Picture, id=id)
    if request.method == 'GET': 
        form = PictureForm(instance=picture) 
        context = { 'form': form, 'picture': picture}
        return render(request, 'edit_picture.html', context)

    elif request.method == 'POST': 
        form = PictureForm(request.POST, instance=picture) 
        if form.is_valid(): 
            update_picture = form.save() 
            return redirect(reverse('picture_details', args=[picture.id]))
        else: 
            context = { 'form': form, 'picture': picture }
            return render(request, 'edit_picture.html', context) 


