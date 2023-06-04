    
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
# Create your views here.
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('tasks')
    
class Tasks(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        login_url = 'login'
        tasks = Task.objects.all().filter(owner=user)
        return render(request, 'home.html', {"tasks":tasks})
class CreateTask(LoginRequiredMixin, View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'create-task.html', {"form":form})
    def post(self, request):
        form  = TaskForm(request.POST)
        form.owner = request.user
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('tasks')
        else:
            return JsonResponse('something went wrong ', safe=False)

class EditTask(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, id=pk)
        form = TaskForm(instance=task)
        return render(request, 'edittask.html', {"form":form})
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            return JsonResponse('something went wrong ', safe=False)
class DeleteTask(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return redirect('tasks')
class FinishTask(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, id=pk)
        task.complated = True
        task.save()
        return redirect('tasks')

class Login(View):
    def get(self, request):
        return render(request, 'login.html', {'login':True})
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('tasks')
        return JsonResponse('username or password didnt match', safe=False)
class RegisterUser(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        name = request.POST['Name']
        email  = request.POST['Email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password!=password2:
            return JsonResponse('password did not mach', safe=False)
        if User.objects.filter(username=email).exists():
            return JsonResponse('user with thisemail already exists!', safe=False)
        user = User.objects.create(username=email,first_name=name)
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('tasks')