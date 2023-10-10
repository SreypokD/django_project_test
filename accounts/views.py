from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dasboardPage(request):
    return render(request, 'accounts/dasboard.html')