from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listings/', views.listings, name='listings'),

    path('session/<int:pk>/', views.sessionDetails, name='sessionDetails'),
    path('session/<int:pk>/update/', views.sessionUpdate, name='sessionUpdate'),
    path('session/<int:pk>/delete/', views.sessionDelete, name='sessionDelete'),
    
    path('session/create/', views.sessionCreate, name='sessionCreate'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name='registerPage'),
]
