from django.urls import path
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:group_id>/', views.detail_student, name='detail_student'),
    path('<str:name>/', views.detail_lecturer, name='detail_lecturer')
]