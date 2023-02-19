from django.shortcuts import render


def ask(request):
    return render(request, 'index.html')

def denial(request):
    return render(request, 'Page1.html')

def denial2(request):
    return render(request, 'Page2.html')

def denial3(request):
    return render(request, 'Page3.html')

def acceptence(request):
    if request.method == "POST":
        date = request.POST.get('when')
        email = request.POST.get('email')
        print(email, date)
        return render(request, 'Page5.html')

    return render(request, 'Page4.html')