from django.shortcuts import render, redirect
from emaillist01 import models

# Create your views here.
def index(request):
    results = models.findAll()
    data = { 'emaillist_list' : results }
    return render(request, 'emaillist01/index.html', data)

def form(request):
    return render(request, 'emaillist01/form.html')

def add(request):
    firstname = request.POST["fn"]
    lastname = request.POST["ln"]
    email = request.POST["email"]

    models.insert(firstname, lastname, email)

    results = models.findAll()
    data = { 'emaillist_list' : results }
    return redirect('emaillist01')