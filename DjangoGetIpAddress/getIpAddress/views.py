from django.shortcuts import render
from django.http import HttpResponse
import socket


# Create your views here.
def index(request):
    return HttpResponse("Ip Address : " + socket.gethostbyname(socket.gethostname()))
