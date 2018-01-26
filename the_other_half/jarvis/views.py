from django.shortcuts import render


def home(request):
	context={}
	return render(request, 'jarvis/home.html', context)
