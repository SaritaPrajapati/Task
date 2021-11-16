from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello Welcome.</h1>")


def hello(request):
    return HttpResponseRedirect('/home')

def joker(request):
    context = {
        "a":10,
        "b":[1,2,3,45,6],
        "name":"Sarita"
    }
    return render (request,'joker.html',context)