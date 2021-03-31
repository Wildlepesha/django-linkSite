from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('available/', views.ShowLinks.as_view(), name='available'),
    path('create/', views.CreateLinkView.as_view(), name='create'),
    path('', views.home, name='home')
]