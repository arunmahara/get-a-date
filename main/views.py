from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage

name = "Momo"

def ask(request):
    return render(request, 'index.html', {'name': name})

def denial(request):
    return render(request, 'Page1.html', {'name': name})

def denial2(request):
    return render(request, 'Page2.html', {'name': name})

def denial3(request):
    return render(request, 'Page3.html', {'name': name})

def acceptence(request):
    if request.method == "POST":
        date = request.POST.get('when')
        email = request.POST.get('email')
    
        email_body = 'Hi, '+ name + "\nI hope this email finds you well. Since you have reached here, it's clear that you've made a good decision. \nThis is an confirmation for our first date, which is scheduled for " + date + ' this week. Looking forward to getting to know you better over some coffee and conversation! \n\nThanks and regards, \nArun'

        email_receive = EmailMessage(
            'Date Corfirmation Mail',   #email subject
            email_body,  #message
            settings.EMAIL_HOST_USER,  #form
            [email] #to
        )

        email_receive.fail_silently=False
        email_receive.send()
        return render(request, 'Page5.html', {'name': name})

    return render(request, 'Page4.html')