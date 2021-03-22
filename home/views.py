from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from amitcoder import settings

# Create your views here.
# @login_required(redirect_field_name='settings.LOGIN_URL')
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

# @login_required(redirect_field_name='settings.LOGIN_URL')
def about(request):
    return render(request,'home/about.html')

# @login_required(redirect_field_name='settings.LOGIN_URL')
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()  #how to create empty queryset in django
    # allPosts=Post.objects.all()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPostsAuthor=Post.objects.filter(author__icontains=query)

        #merge two queryset
        allPosts1=allPostsTitle.union(allPostsContent)
        allPosts=allPosts1.union(allPostsAuthor)
    if allPosts.count()==0: # how to find length of queryset in django
        messages.error(request,"No search results found please refine your query")
    params={"allPosts":allPosts,"query":query}
    return render(request,'home/search.html',params)

def signup(request):
    if request.method=='POST':
        # Get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # Checks for errorneous inputs
        # username must less than 10 characters
        if len(username)>10:
            messages.error(request,"Username must be under 10 character")
            return redirect("home")

        # password must match
        if pass1 !=pass2:
            messages.error(request,"password do not match")
            return redirect("home")
        #username must be alphanumeric
        if not username.isalnum():
            messages.error(request,"username should only contain letters and digits")
            return redirect("home")

        # create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your AmitCoder account is created sucessfully")
        return redirect('home')
    else:
        return HttpResponse("<h1>404-Not Found</h1>")


def handlelogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['pass']

        # we check in database for such user 
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect("home")
        else:
            messages.error(request,"Invalid Credentials ,Please try again")
            return redirect("home")
    else:
        return HttpResponse("<h1>404-Not Found</h1>")

def handlelogout(request):
        # logout whoever is logged in
        logout(request)
        messages.success(request,"successfully logged out")
        return redirect("home")




