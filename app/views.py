from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def weather(request):
    return render(request, 'weather.html')
def about(request):
    return render(request, 'about.html')


def ecart(request):
    return render(request, 'ecart.html')
def marketrate(request):
    return render(request, 'marketrate.html')
def plantingmaterials(request):
    return render(request, 'plantingmaterials.html')


def tips(request):
    return render(request, 'tips.html')
def gallery(request):
    return render(request, 'gallery.html')
def contact(request):
    return render(request, 'contact.html')
