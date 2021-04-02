from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello1(request):
    return HttpResponse("hello1")

def hello2(request):
    return render(request, 'helloword/hello2.html')

def tags(request):
    return render(request, 'helloword/tags.html')