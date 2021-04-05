from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'helloword/main.html')

def hello1(request):
    name = request.GET['name']
    return HttpResponse(f"어서오세요 {name} 님")

def tags(request):
    return render(request, 'helloword/tags.html')

def form(request):
    return render(request, 'helloword/form.html')

def join(request):
    username = request.POST['username']
    password = request.POST['password']
    gender = request.POST['gender']
    hobby = request.POST.getlist['hobby']
    description = request.POST['desc']

    return HttpResponse("ok")