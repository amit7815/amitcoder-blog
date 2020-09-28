from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2 or len(email)<10  or len(phone)<10 or len(content)<4:
            messages.error(request,"please fill the form correctly")
        else:
        #print(name,email,phone,content)
            contact=Contact(name=name,phone=phone,email=email,content=content)
        #for saving in database
            contact.save()
            messages.success(request,"Your message has been successfully sent")
    return render(request,'home/contact.html')

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')


