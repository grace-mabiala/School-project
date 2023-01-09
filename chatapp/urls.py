from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home,name='home'),
    path('chat', views.message,name='message'),
    path('register', views.register,name='register'),
    path('messagebox', views.message_box,name='message_box'),
    path('', views.logout_view,name='logout_view'),
    path('<int:id>', views.deletemessage,name='delete'),
]
