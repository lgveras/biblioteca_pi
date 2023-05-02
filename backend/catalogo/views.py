from django.shortcuts import render
from .models import Editora
from django.http import HttpResponse

def index(request):
    editora = Editora()
    return HttpResponse(editora)
    # return HttpResponse("INDEX")
