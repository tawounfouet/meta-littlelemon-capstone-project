from django.shortcuts import render
from django.http import HttpResponse


def sayHello(request):
 return HttpResponse('Hello World')


# Create your views here.
def index(request):
    return render(request, 'index.html', {})