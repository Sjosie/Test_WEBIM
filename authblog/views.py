from django.shortcuts import render
from .models import Greetings

def post_list(request):
    posts = Greetings.objects.all()
    return render(request, 'authblog/post_list.html', {'posts': posts})

