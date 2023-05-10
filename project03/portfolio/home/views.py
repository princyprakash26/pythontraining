from django.shortcuts import render,HttpResponse
from home.models import Contact


# Create your views here.

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,"about.html")
def contact(request):
    #forms are handle here
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        description=request.POST['description']
        c=Contact(name=name,email=email,phone=phone,description=description)
        c.save()
    return render(request,"contact.html")
