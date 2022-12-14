from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'index.html')

def about(requests):
    return render(requests, 'about.html')

def contact(requests):
    return render(requests, 'contact.html')

def portfolio(requests):
    return render(requests, 'portfolio.html')

def price(requests):
    return render(requests, 'price.html')

def services(requests):
    return render(requests, 'services.html')

