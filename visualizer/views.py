from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

# save data to database
def save(request):
	return HttpResponse('Hello, World!')

# get data to draw
def draw(request):
	return HttpResponse('Hello, World!')