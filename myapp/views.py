from django.shortcuts import render

# Create your views here.
def home(request):  
    return render(request, 'home.html')



from django.core.mail import send_mail
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        send_mail(
            subject,
            f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}',
            email,
            ['nkosi9976@gmail.com'],
            fail_silently=False,
        )
        
        return HttpResponse('Your message has been sent. Thank you!')