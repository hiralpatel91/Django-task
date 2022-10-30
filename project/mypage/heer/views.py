from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Add
from .forms import AddForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def registerview(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        usr = User(username=username , email=email)
        usr.set_password(password)
        usr.save()
    
    return render(request,'Register.html')

def logindata(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        usr = authenticate(username=username , password=password)
        
        if usr is None:
            messages.info(request,'invalid user')
            return redirect('login')
        
        login(request, usr)
        return redirect('home')
    
    
    return render(request,'login.html')

def logoutdata(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')

def addview(request):
    if request.method == 'POST':
       name = request.POST['name'] 
       branch = request.POST['branch'] 
       language = request.POST['language'] 
       field = request.POST['field'] 
       technical_language = request.POST['technical_language'] 
       
       add = Add(name=name,branch=branch,language=language,field=field,technical_language=technical_language)
       add.save()
       
    all_add = Add.objects.all()

    
    return render(request,'add.html', {'all_add':all_add})

def editview(request, id):
    if request.method == 'POST':
        edit = Add.objects.get(pk=id)
        form = AddForm(request.POST, instance=edit)
        
        if form.is_valid():
            form.save()
            
    else:
        edit = Add.objects.get(pk=id)
        form = AddForm(instance=edit)

    return render(request, 'edit.html', {'form':form})

def deleteview(request,id):
    dlt = Add.objects.get(pk=id)
    dlt.delete()
    
    return redirect('add')
    
