
from django.urls import path
from . import views
urlpatterns = [
     path('tasks/', views.Tasks.as_view(), name='tasks'),
     path('delete-task/<int:pk>', views.DeleteTask.as_view(), name="delete_task"),
     path('create-task',views.CreateTask.as_view(), name="create-task"),
     path('accounts/login/', views.Login.as_view(), name="login"),
     path('register/', views.RegisterUser.as_view(), name="register"),
     path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
     path('edit-task/<int:pk>', views.EditTask.as_view(), name="edit_task"),
     path('finish-task/<int:pk>', views.FinishTask.as_view(), name="finish_task"),
]