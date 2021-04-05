from django.shortcuts import render, redirect
from guestbook01 import models

# Create your views here.
def index(request):
    results = models.findAll()
    data = { 'guestbook_list' : results }
    return render(request, 'guestbook01/index.html', data)

def deleteform(request):
    return render(request, 'guestbook01/deleteform.html', no_data)

def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    models.insert(name, password, message)

    return redirect('guestbook01')

def delete(request):
    no = request.POST['no_data']
    password = request.POST['password2']

    models.removeby_no_and_pass(no, passowrd2)
    
    return redirect('guestbook01')