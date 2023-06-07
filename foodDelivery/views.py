# created
#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from foodtiger.models import Contact, MenuItem, Category, OrderModel
from django.views import View
#from .models import MenuItem, Category, OrderModel
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request):
   return render(request,'index.html')

def contact(request):
    context={}
    if request.method=="POST":
       name = request.POST.get("name")
       em = request.POST.get("email")
       sub = request.POST.get("address")
       mes = request.POST.get("fooditem")

       obj = Contact(name=name, email=em, address=sub, fooditem=mes )
       obj.save()
       context['message']= f"Dear {name} Thanks for ordering! "
    return render(request,'contact.html',context)

def about(request):
   return render(request,'about.html')

def booking(request):
   return render(request,'booking.html')

def blog(request):
   return render(request,'blog.html')

def menu(request):
   return render(request,'menu.html')


def SignupPage(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:

            context['message'] = f"Your password and confrime password are not Same!! "
            return render(request, 'signup.html',)

        else:
              my_user = User.objects.create_user(uname, email, pass1)
              my_user.save()
        context['message'] = f"Dear{my_user} Well done  !!! "
        return redirect('login')

    return render(request, 'signup.html',context)


def LoginPage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)

            return redirect("index")
        else:
             return redirect("login")

    return render (request,'login.html')

def LogoutPage(request):

    logout(request)

    return redirect('login')




def Order(request):

    if request.method == 'POST':
        # get every item from each category
        appetizers = request.POST.get('Appetizer')
        entres = request.POST.get('Entre')
        desserts = request.POST.get('Dessert')
        drinks = request.POST.get('Drink')
        obj = OrderModel(Appetizer=appetizers, Entre=entres, Dessert=desserts, Drink=drinks)
        obj.save()
        # pass into context

        # render the template
    return render(request, 'order.html')

def ordernow(request):
    return render(request, 'order.html')
