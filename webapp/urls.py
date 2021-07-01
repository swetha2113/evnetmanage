from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name="home"),
    path('check',views.check,name="check"),
    path('about',views.about,name="about"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('search',views.search,name="search"),
    path('result1',views.result1,name="result1"),
    path('<int:id>',views.details,name="details"),
    path('like_post',views.like_post,name="like_post"),
]