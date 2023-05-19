from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html', {})


def contact_us(request):
    return render(request, 'home/contact_us.html', {})
