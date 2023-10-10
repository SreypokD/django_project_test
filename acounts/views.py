from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return HttpResponse('wellcome to home page')

def productPage(request):
    return HttpResponse('wellcome to product page')

def customerPage(request):
    return HttpResponse('wellcome to customer page')
