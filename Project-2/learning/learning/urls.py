from learning.view import home # function for route 
from django.contrib import admin
from django.urls import path
from learning.view import about,createblog,allblogs

urlpatterns = [
    path('admin/', admin.site.urls),  #(route , function)
    path('',home),
    path('about',about),
    path('createblog',createblog),
    path('blogs',allblogs)
]
