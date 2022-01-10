from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'index.html')

def profile(request):
	return render(request, 'index.html')

def create(request):
	return render(request, 'index.html')

def homeless(request):
	return render(request, 'index.html')

def pets(request):
	return render(request, 'index.html')

def edit(request):
	return render(request, 'index.html')