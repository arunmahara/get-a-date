from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage

name = "Jessica"
count = 0

def ask(request):
    print("\n********** on index page **********\n")
    return render(request, 'index.html', {'name': name})

def denial(request):
    print("\n********** on denial page 1 **********\n")
    return render(request, 'Page1.html', {'name': name})

def denial2(request):
    print("\n********** on denial page 2 **********\n")
    return render(request, 'Page2.html', {'name': name})

def denial3(request):
    print("\n********** on denial page 3 **********\n")
    global count
    count += 1
    print(f"\n********** Please Count {count-1} **********\n") if count > 1 else None
    return render(request, 'Page3.html', {'name': name, 'count': count-1})

def acceptence(request):
    if request.method == "POST":
        print("\n********** form filled **********\n")
        date = request.POST.get('when')
        email = request.POST.get('email')
    
        email_body = 'Hi, '+ name + "\nI hope this email finds you well. Since you have reached here, it's clear that you've made a good decision. \nThis is an confirmation for our pizza date, which is scheduled for " + date + '. Looking forward to getting to know you better over some pizza and conversation! \n\nThanks and regards, \nArun'

        email_receive = EmailMessage(
            'Pizza Date Confirmation Mail',   #email subject
            email_body,  #message
            settings.EMAIL_HOST_USER,  #form
            [email] #to
        )

        email_receive.fail_silently=False
        email_receive.send()
        print("\n********** email sent **********\n")
        return render(request, 'Page5.html', {'name': name})

    print("\n********** on acceptence page **********\n")
    return render(request, 'Page4.html')
