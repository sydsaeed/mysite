from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(requests):
    return HttpResponse("<h1>Home page</h1>")

def about_view(requests):
    return HttpResponse("<h1>about page</h1>")

def contact_view(requests):
    return HttpResponse("<h1>contact page</h1>")

