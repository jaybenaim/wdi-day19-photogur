from django.db import models 
from django import forms 
from django.forms import ModelForm 



class Picture(models.Model): 
    title = models.CharField(max_length=225)
    artist = models.CharField(max_length=225) 
    url = models.CharField(max_length=225)
    
    def __str__(self): 
        return f'{self.title}'


class Comment(models.Model): 
    name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    message = models.TextField() 
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='comments')

    def __str__(self): 
        return f'{self.message}'

  
class PictureForm(ModelForm): 
    class Meta: 
        model = Picture 
        fields = ['title', 'artist', 'url']
        