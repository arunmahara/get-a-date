from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage

name = "Ruks"
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
        # date = request.POST.get('when')
        # email = request.POST.get('email')
    
        email_body = 'Hi, '+ name + "❤️\n\nI hope this message brings a smile to your face😄. Since you've found your way here, it's clear you've already made the best decision—saying yes to be my Valentine💘.\nThis is just a little confirmation that you'll be my Valentine, not just for today, but forever and ever. I'm so happy to have you in my life🥰 and I can't wait to create more beautiful memories together✨.\nUntil then, keep this thought close: you're pretty amazing💃🏻🌟.\n\nWith all my heart,\nArun🫶🏻"

        email_receive = EmailMessage(
            '💌 A Special Message Just for You 💌',   #email subject
            email_body,  #message
            settings.EMAIL_HOST_USER,  #from
            [settings.EMAIL_TO] #to
        )

        email_receive.fail_silently=False
        email_receive.send()
        print("\n********** email sent **********\n")
        return render(request, 'Page5.html', {'name': name})

    print("\n********** on acceptence page **********\n")
    return render(request, 'Page4.html')
