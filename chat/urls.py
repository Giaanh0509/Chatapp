from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    #path('<str:room>/', views.room, name='room'),
    path('<str:room>/', views.room, name='room'),
    path('', views.room1, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]


