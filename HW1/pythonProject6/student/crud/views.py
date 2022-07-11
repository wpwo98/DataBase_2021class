from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Students
# Create your views here.

def add(request):
    form = StudentForm(request.POST or None)
    #student = Students.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form': form})

def show(request):
    student = Students.objects.all()
    return render(request, 'show.html', {'student': student})

def update(request, id):
    before_id = request.GET['before_ID']
    students = Students.objects.get(id=before_id)
    form = StudentForm(request.POST, instance=students)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'students': students})

def delete(request, id):
    form = Students.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')

def deleteAll(request):
    form = Students.objects.all()
    form.delete()
    return HttpResponseRedirect('/')
