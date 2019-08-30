from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path('question/', views.index2, name='index2'),
    path('question/answer/<int:qno>/', views.index3, name='index3'),
    path('question/pushinbuffer/<int:qno>/', views.buffer, name='buffer'),
    path('question/logout/', views.index4, name='login_logout'),
]
