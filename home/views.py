from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'home/contact.html')

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')


