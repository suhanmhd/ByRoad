
from django.shortcuts import render,redirect
from django.contrib import messages
from map.views import *
from map.models import Usermapping
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required 


# USER REGISTRATION
def signup(request):
    if request.method=='POST':
        a=request.POST['uname']
        b=request.POST['fname']
        c=request.POST['lname']
        d=request.POST['email']
        e=request.POST['pwd']
        f=request.POST['cpwd']
        if e==f:
            if User.objects.filter(username=a):
                messages.warning(request,'user name already taken')
            
               
                return render(request,'auth/signup.html') 
            elif User.objects.filter(email=d):
                 messages.warning(request,'email  already taken') 
                 return render(request,'auth/signup.html')
            else:
                User.objects.create_user(username=a,first_name=b,last_name=c,email=d,password=e).save() 
                messages.success(request,'Registered Successfully! Login to Continue')
                return redirect(user_login)       

        else:
            messages.warning(request,'password not matching')
            return render(request,'auth/signup.html') 
      
    return render(request,'auth/signup.html') 


def user_login(request):

    if request.user.is_authenticated:
        messages.success(request,"you are already Logined")

        return redirect(userhome)
    else: 
        if request.method=='POST':

            a=request.POST['lgname']
            b=request.POST['lgpwd']

            user=auth.authenticate(username=a,password=b)
            if user is not None:
           
                login(request,user)
                messages.success(request,"Login successfully")
                return redirect(userhome)
            else:
                messages.warning(request,'invalid username or password')
            
                return render(request,'auth/login.html')   
 
        return render(request,'auth/login.html')

# Traffic REGISTRATION

def traffic_signup(request):
    if request.method=='POST':
        a=request.POST['uname']
        b=request.POST['fname']
        c=request.POST['lname']
        d=request.POST['email']
        e=request.POST['pwd']
        f=request.POST['cpwd']
        if e==f:
            if User.objects.filter(username=a):
                messages.warning(request,'user name already taken')
            
               
                return render(request,'stores/auth/signup.html') 
            elif User.objects.filter(email=d):
                 messages.warning(request,'email  already taken') 
                 return render(request,'auth/signup.html')
            else:
                User.objects.create_user(username=a,first_name=b,last_name=c,email=d,password=e).save() 
                messages.success(request,'Registered Successfully! Login to Continue')
                return redirect(user_login)       

        else:
            messages.warning(request,'password not matching')
            return render(request,'auth/signup.html') 
      
    return render(request,'auth/signup.html') 


def traffic_login(request):

    if request.method=='POST':
        loginname=request.POST['lgname']
        loginpassword=request.POST['lgpwd']

        user=auth.authenticate(username=loginname,password=loginpassword)
        if user is not None:
            if Usermapping.objects.filter(user=user,is_traffic=True):
                 login(request,user)
                 return redirect(trafficdept)
           
           
            else:
                messages.warning(request,'invalid username or password')
                print('invalid username or password')
                return render(request,'auth/trafficlogin.html')   
    
        else:
                messages.warning(request,'invalid username or password')
                print('invalid user')
                return render(request,'auth/trafficlogin.html') 
 
    return render(request,'auth/trafficlogin.html')

def pwd_login(request):

    if request.method=='POST':
        loginname=request.POST['lgname']
        loginpassword=request.POST['lgpwd']

        user=auth.authenticate(username=loginname,password=loginpassword)
        if user is not None:
            if Usermapping.objects.filter(user=user,is_pwd=True):
                 login(request,user)
                 return redirect(roads)
           
           
            else:
                messages.warning(request,'invalid username or password')
                print('invalid username or password')
                return render(request,'auth/pwdlogin.html')   
    
        else:
                messages.warning(request,'invalid username or password')
                print('invalid user')
                return render(request,'auth/pwdlogin.html') 
 
    return render(request,'auth/pwdlogin.html')



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout successfully")
    return redirect(home)
        
    
   


