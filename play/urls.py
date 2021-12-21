from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_singleplayer/', views.start_singleplayer, name='start_singleplayer'),
    path('rules/', views.rules, name='rules'),
    path('submit_name/', views.submit_name, name='submit_name'),
    path('random_move/', views.random_move, name='random_move'),
    path('center_return/', views.center_return, name='center_return'),
    path('singleplayer/', views.singleplayer, name='singleplayer'),
]


