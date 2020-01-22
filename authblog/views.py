from django.shortcuts import render
from django.http import JsonResponse
from .models import Greetings
import urllib.request, json
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.generic.detail import BaseDetailView
from json_tag.views import JsonResponseMixin
from django.db import models
from django.views.generic.base import View
from json_tag.views import JsonRequestMixin
from json_tag.http import JsonResponse
from django import template
from django.template import RequestContext, Template
# from . import LoginForm, SignupForm

def post_list(request):
    
    posts = Greetings.objects.all()
    return render(request, 'authblog/post_list.html', {'posts': posts})


def logout(request):
    auth.logout(request)
    return redirect(get_next_url(request))
    

def login(request, *args, **kwargs):
    username = {{ user.get_username }}
    usernamelist = []
    usernamelist.append(username)

    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return auth_views.login(request, *args, **kwargs)


# class Blog(models.Model):
#     title = models.CharField(max_length=255)
#     body = models.TextField()

#     def to_json(self):
#         return {
#             'title': self.title,
#             'body': self.body,
#         }

# class BlogDetailView(JsonResponseMixin, BaseDetailView):
#     """
#     Detail view returning object serialized in JSON
#     """
#     model = Blog

# class EchoView(JsonRequestMixin, View):
#     def dispatch(self, *args, **kwargs):
#         return JsonResponse(self.data())


# def show_auth(request):
#     return render(request, 'authblog/post_list.html', {'singup_form': SignupForm(), 'login_form': LoginForm()})