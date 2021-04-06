from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from guestbook02.models import Guestbook

# Create your views here.
def index(request):
    results = Guestbook.objects.all().order_by('-id')
    data = { 'guestbook_list' : results }
    return render(request, 'guestbook02/index.html', data)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return redirect('guestbook02')

def deleteform(request):
    return render(request, 'guestbook02/deleteform.html')

def delete(request):
    guestbook = Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password'])
    guestbook.delete()
 
    return redirect('guestbook02')