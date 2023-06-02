from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home/index.html', {})


def contact_us(request):
    if request.method == "POST":
        client_name = request.POST['name']
        client_email = request.POST['email']
        client_phone = request.POST['phone']
        client_message = request.POST['message']

        # send email
        send_email(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['greg.nnabuife.code@gmail.com'],  # to email
            fail_silently=False
        )

        return render(request, 'home/contact_us.html', {'client_name': client_name})
    else:
        return render(request, 'home/contact_us.html', {})


def about_us(request):
    return render(request, 'home/about_us.html', {})


def services(request):
    return render(request, 'home/services.html', {})


def blog(request):
    return render(request, 'home/blog.html', {})
