from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import upload_product
from django.utils import timezone
from datetime import datetime

# Create your views here.
def Home(Request):
    return render(Request,'index.html')

def user_login(request):
    if request.method =='POST':
        username=request.POST['uname']
        password=request.POST['pass']
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            uname = user.username
            return render(request,'index.html',{'uname':uname})
        else:
            return redirect('login')
    return render(request,'login.html')

def signup(request):
     if request.method == "POST":
         username=request.POST['uname']
         phonenum=request.POST['phno']
         password=request.POST['pass']
         cpassword=request.POST['cpass']

         myuser =User.objects.create_user(username,phonenum,password)
         myuser.save()
         return redirect('login')
     return render(request,'signup.html')
def user_logout(request):
    logout(request)
    return redirect('home')


def shop(request):
    products=upload_product.objects.all()
    return render( request,'shop.html',{'products':products})


def adminlte(request):
    if request.method == 'POST':
        product_id = request.POST.get('prod_id')
        product_name = request.POST.get('prod_n')
        product_title = request.POST.get('prod_t')
        product_desc = request.POST.get('description')
        product_mrp = request.POST.get('prod_p')
        product_disc = request.POST.get('prod_d')
        product_c = request.POST.get('prod_c') 
        if 'image' in request.FILES:
            product_img = request.FILES['image']
        else:
            return HttpResponse("No image file uploaded.", status=400)
        user = upload_product(product_id, product_title, product_name, product_mrp, product_disc, product_img, product_c)
        user.save()

        return redirect('adminlte')

    return render(request, 'adminlte.html')

def buy(request):
    return render(request, 'buy.html') 

def cart(request):
    return render(request,'cart.html')





def mobiles(request):
    return render(request,'mobiles.html')
def laptops(request):
    return render(request,'laptops.html')
def tabs(request):
    return render(request,'tabs.html')
def accessories(request):
    return render(request,'accessories.html')
def headsets(request):
    return render(request,'headsets.html')
def watches(request):
    return render(request,'watches.html')
def televisions(request):
    return render(request,'televisions.html')
