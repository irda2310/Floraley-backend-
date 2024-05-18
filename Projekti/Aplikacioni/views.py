from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


# Create your views here.
def navbar (request):
     prodShop = Shop.objects.all().order_by("-shop_id")
     kategorit = Kategoria.objects.all().order_by("-kategoria_id")
     blogs=Blog.objects.all().order_by("-blog_id")
     fullblogs = Fullblog.objects.all()
     context = {"prodShop":prodShop, "kategorit":kategorit, "blogs":blogs, "fullblogs":fullblogs}

     if request.method == 'POST':
        name_ = request.POST.get('name_', '')
        email = request.POST.get('email', '')

        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, 'Email is already registered.')  # Display a warning message
            else:
                subscriber = Subscriber(name=name_, email=email)
                subscriber.save()
                messages.success(request, 'You have been successfully registered.')  # Display a success message
        else:
            messages.warning(request, 'Invalid email.')  # Display a warning message for invalid email

     return render (request,"navbar.html",context)
   

def about (request):
     kategorit = Kategoria.objects.all().order_by("-kategoria_id")
     reviews=Review.objects.all()
     context = {"kategorit":kategorit, "reviews":reviews}
     return render (request, "about.html",context)


def blog (request,id):
     kategorit = Kategoria.objects.all().order_by("-kategoria_id")
     fullblogs = Fullblog.objects.get(fullblog_id=id)
     context={"fullblogs":fullblogs, "kategorit":kategorit}
     return render (request, "blog.html", context)

def contact (request):
     kategorit = Kategoria.objects.all().order_by("-kategoria_id")
     context = {"kategorit":kategorit}
     if request.method =='POST':
          name_=request.POST['name_'] 
          email=request.POST['email']
          message=request.POST['message']
          Contact (contact_name=name_,contact_message=message,contact_email=email).save()
                   
                   
          messages.success(request,'Your message was sent successfully')
     return render(request, 'contact.html', context)

def shop (request,id):
     kategorit = Kategoria.objects.all().order_by("-kategoria_id")
     detShop =  Kategoria.objects.get(kategoria_id=id)
     prodShop = Shop.objects.filter(shop_category=detShop).order_by("-shop_id")
     context = {"prodShop":prodShop, "kategorit":kategorit}
     return render (request, "shop.html",context)




     # User
def register(request):
    kategorit = Kategoria.objects.all().order_by("-kategoria_id")
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        login_form = LoginForm(request, data=request.POST)
        
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
        
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('/')
    else:
        register_form = RegisterForm()
        login_form = LoginForm()
    
    context = {
        'register_form': register_form,
        'login_form': login_form, 
        "kategorit":kategorit
    }
   

    return render(request, 'user/register.html', context)

def logout_view(request):
    auth.logout(request)
    return redirect('/')


  

