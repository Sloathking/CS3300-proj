from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listings/', views.listings, name='listings'),

    path('session/<int:pk>/', views.sessionDetails, name='sessionDetails'),
    path('session/<int:pk>/update/', views.sessionUpdate, name='sessionUpdate'),   
]
