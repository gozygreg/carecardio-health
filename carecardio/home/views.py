from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html', {})


def contact_us(request):
    if request.method == "POST":
        client_name = request.POST['name']
        client_email = request.POST['email']
        client_phone = request.POST['phone']
        client_message = request.POST['message']
        return render(request, 'contact_us.html', {'client_name':client_name})
    else:
        return render(request, 'home/contact_us.html', {})
