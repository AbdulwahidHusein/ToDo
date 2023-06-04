    
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from .forms import TaskForm
# Create your views here.

class Tasks(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'home.html', {"tasks":tasks})
class CreateTask(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'create-task.html', {"form":form})
    def post(self, request):
        return

class EditTask(View):
    def get_object(self, pk):
        return Task.objects.get(pk=pk)
    def get(request):
        return
    def post(self, request):
        return
class DeleteTask(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return redirect('tasks/')
class Login(View):
    def get(self, request):
        return render(request, 'login.html', {'register':True})
class RegisterUser(View):
    def get(request):
        return render(request, 'login.html')
    def post(request):
        return render('tasks/')