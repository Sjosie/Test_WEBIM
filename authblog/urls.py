from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('logout/', views.logout, name='logout'),
]