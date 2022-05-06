from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import POST
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.

def send_message(request):
    send_mail("Web programming:backend" , "This is my text for your email",
              "onbolsyn.serik@gmail.com",["200103233@stu.sdu.edu.kz"],
              fail_silently=False,html_message="<b>Bold text</b>")
    return render(request,"main/lab5.html")


def send_message1(request):
    email=EmailMessage('Hi','This is the second type of sending emails','onbolsyn.serik@gmail.com',
                       ['200103233@stu.sdu.edu.kz'],headers={'Message-ID':'foo'})
    email.attach_file('C:/Users/onbol/OneDrive/Изображения/sd.png')
    email.send(fail_silently=False)
    return render(request,"main/lab5.html")

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
           form.save()



        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})