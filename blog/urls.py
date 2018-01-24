from django.urls import path

from . import views

urlpatterns = [
    #ex: /blog/
    path('', views.post_list, name='post_list'),
    # ex: /blog/
]    