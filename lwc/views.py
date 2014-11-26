from django.shorcuts import render


def home(request):
	context = {}
	template = "home.html"
	return render(request, template, context);

def home2(request):
	context = {}
	template = "home.html"
	return render(request, template, context);