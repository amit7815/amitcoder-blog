from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        #print(name,email,phone,content)
        contact=Contact(name=name,phone=phone,email=email,content=content)
        #for saving in database
        contact.save()
    return render(request,'home/contact.html')

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')


