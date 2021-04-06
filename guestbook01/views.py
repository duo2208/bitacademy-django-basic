from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from guestbook01 import models

# Create your views here.
def index(request):
    results = models.findAll()
    data = { 'guestbook_list' : results }
    return render(request, 'guestbook01/index.html', data)

def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    models.insert(name, password, message)

    return redirect('guestbook01')

def deleteform(request):
    return render(request, 'guestbook01/deleteform.html')

def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    models.removeby_no_and_pass(no, password)

    return redirect('guestbook01')