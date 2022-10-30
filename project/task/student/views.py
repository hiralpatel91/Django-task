from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages



# Create your views here.

def frontview(request):
    return render(request, 'front.html')

def registerview(request):
    if request.method == 'POST':
        email = request.POST['email']
        fullname = request.POST['fullname']
        username = request.POST['username']
        branch = request.POST['branch']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        
        usr = User(email=email,username=username)
        usr.set_password(password)
        usr.save()
    # all_user = User.objects.all()    

    return render(request, 'register.html',)#{'all_user':all_user}

def logindata(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        usr = authenticate(username=username ,email=email,  password=password)
        
        if usr is None:
            messages.info(request,'invalid user')
            return redirect('login')
        
        login(request, usr)
        return redirect('front')
    
    return render(request,'login.html')

def logoutdata(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('front')
