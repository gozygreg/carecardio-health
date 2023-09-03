from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from carecardioblog.models import Post
from carecardioblog.forms import PostForm


def home(request):
    return render(request, "home/index.html", {})


def contact_us(request):
    if request.method == "POST":
        client_name = request.POST["name"]
        client_email = request.POST["email"]
        client_phone = request.POST["phone"]
        client_message = request.POST["message"]

        # send email
        send_mail(
            client_name,  # subject
            client_message,  # message
            client_email,  # from email
            ["gregmeditechinc@gmail.com"],  # to email
            fail_silently=False,
        )

        # Add success message
        messages.success(
            request,
            "Thank you, Your email sent successfully! We will get back to you shortly",
        )
        return redirect("about_us.html")

        # return render(request, 'home/contact_us.html', {'client_name': client_name})
    else:
        return render(request, "home/contact_us.html", {})


def about_us(request):
    return render(request, "home/about_us.html", {})


def services(request):
    return render(request, "home/services.html", {})


# def blog(request):
#     return render(request, 'home/blog_list.html', {})


def post_list(request):
    posts = Post.objects.all()
    return render(request, "home/blog_list.html", {"posts": posts})
