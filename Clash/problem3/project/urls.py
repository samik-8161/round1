from django.urls import path
from project import views

urlpatterns = [
    path('', views.index1),
    path('question/', views.index2, name='index2'),
    path('question/answer/<int:qno>/', views.index3, name='index3'),
    path('question/result_page/', views.login_logout, name='login_logout')
]
