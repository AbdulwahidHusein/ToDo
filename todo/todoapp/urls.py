
from django.urls import path
from . import views
urlpatterns = [
     path('tasks', views.Tasks.as_view(), name='tasks'),
     path('delete-task/<int:pk>/', views.DeleteTask.as_view(), name="delete_task"),
     path('create-task',views.CreateTask.as_view(), name="create-task"),
     path('login/', views.Login.as_view(), name="login"),
]