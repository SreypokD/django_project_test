from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dasboardPage(request):
    context = {
        "first_name" : "Suskith",
        "last_name"  : "Arora",
    }
    return render(request, 'accounts/dasboard.html' ,context)
