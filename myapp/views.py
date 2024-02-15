from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginuser
from .forms import CustomUserCreationForm
# Create your views here.
def home(request):
    return render(request,'myapp/index.html')

def login(request):
   if request.method == "GET":
    
        form = AuthenticationForm()
        context={
            "form":form
        }
        return render(request,'myapp/login.html',context = context)
   else:
       form = AuthenticationForm(data = request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user  = authenticate(username = username , password = password)
           if user is not None:
               loginuser(request,user)
               return redirect('home')


       else:
           context={
            "form":form
        }
       return render(request,'myapp/login.html',context = context)
           

def signup(request):
   if request.method == "GET":
        
        form = CustomUserCreationForm()
        context = {
            "form":form
        }
        return render(request,'myapp/signup.html',context=context)
   else:
       form = CustomUserCreationForm(request.POST)
       context = {
            "form":form
        }
       if form.is_valid():
          user = form.save()
          return redirect('login')


      
       else:
           print(form.errors)
           return render(request,'myapp/signup.html',context=context)
       

