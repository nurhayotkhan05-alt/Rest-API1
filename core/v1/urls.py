from django.urls import path

from .views import *

urlpatterns = [
    path('product/',product_list),
    path('product/create',product_create),
    path('product/delete/<int:pk>/',product_delete),
    path('users/',UserList.as_view()),
    path('student/',StudentList.as_view()),
    path('student/<int:pk>',StudentList.as_view()),
]