from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('index', views.index),  # book imformation page
    path('create', views.create),  # create a new book
    re_path('delete(\d+)', views.delete),  # delete book
    path('areas', views.areas),  # self match
]
