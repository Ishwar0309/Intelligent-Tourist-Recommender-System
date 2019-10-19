from django.shortcuts import render,redirect
from loginModule.models import *
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def home(request):
    return render(request,"loginModule/home.html")

def loginView(request):
    if request.method == 'POST':
        formData = request.POST
        emailId = formData['emailId']
        password = formData['password']
        try:
            queryCheck = User.objects.get(emailId=emailId)
            passwordActual = queryCheck.password
            message = {}
            if password == passwordActual:
                print('hua')
                return render(request, "tourism/home.html")
            else:
                print('galat pass')
                message['message'] = "Invalid Credentials"
            return render(request,"loginModule/login.html",message)
        except Exception as e:
            print(e)
            return render(request, "loginModule/signUp.html")
    return render(request,"loginModule/login.html")


def signUpView(request):
    if request.method == 'POST':
        formData = request.POST
        email = formData['email']
        phoneNo = formData['phoneNo']
        username = formData['username']
        password = formData['password']
        confirmPassword = formData['confirmpassword']
        try:
            queryCheck = User.objects.get(emailId=email)
            message = {}
            message['message'] = "User Already exists"
            return render(request,"loginModule/signUp.html",message)
        except Exception as e:
            print(e)
            user = User(emailId=email, password=password, userName=username, phoneNo=phoneNo)
            # profile.save()
            user.save()
            # messages.success(request,f'Account created! You can now login')
            return render(request, "loginModule/login.html")
        # profile = Profile()
    return render(request,"loginModule/signUp.html")



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            # messages.success(request,f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'loginModule/signUp.html' , {'form' : form })
   
