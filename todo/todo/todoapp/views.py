from django.shortcuts import render
from django.views import View
from .models import Task
# Create your views here.

class Tasks(View):
    def get(request):
        return render(request, 'home.html')
class CreateTask(View):
    def get(request):
        return
    def post(request):
        return

class EditTask(View):
    def get_object(self, pk):
        return Task.objects.get(pk=pk)
    def get(request):
        return
    def post(request):
        return
    
