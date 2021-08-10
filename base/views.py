from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def test2(request):
	return render(request, 'base/test2.html')

def test3(request):
	return render(request, 'base/test3.html')

def test4(request):
	return render(request, 'base/test4.html')
