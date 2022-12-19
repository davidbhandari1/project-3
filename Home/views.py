from django.shortcuts import render
from .models import *
# Create your views here.
def home(requests):
    return render(requests, 'index.html')

def about(requests):
    return render(requests, 'about.html')

def contact(requests):
    if requests.method =='POST':
        name = requests.POST['name']
        email = requests.POST['email']
        subject = requests.POST['subject']
        message = requests.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        message ={'mess':'the message is submitted'}
        return render(requests, 'contact.html',message )

    return render(requests, 'contact.html', )

def portfolio(requests):
    return render(requests, 'portfolio.html')

def price(requests):
    return render(requests, 'price.html')

def services(requests):
    return render(requests, 'services.html')

