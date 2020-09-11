from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Stud
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/display")
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')

    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['confirm']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.save()
                phone = request.POST['phone']
                grade = request.POST['grade']
                newuser = Stud(phone=phone, grade=grade, name=user)
                newuser.save()
                messages.success(request,'User Created Successfully!!')
                return redirect('/login')

        else:
            messages.error(request,'Password not Matching...')
            return redirect('/register')
        redirect('/')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def change_paswd(request):
    if request.method=='POST':
        current = request.POST['opswd']
        new = request.POST['npswd']
        cnf_new = request.POST['cpswd']
        user = User.objects.get(id = request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==False:
            messages.warning(request,'Incorrect Current Password')
            return redirect('/changepaswd')
        else:
            if(new==cnf_new):
                user.set_password(new)
                user.save()
                messages.success(request, 'Password changed successfully!!')
                user = User.objects.get(username=un)
                auth.login(request,user)
                return redirect('/changepaswd')
    else:
        return render(request,"change_pwd.html")

def display(request):
    data = Stud.objects.filter(name_id = request.user)
    return render(request, "display.html", {'data': data})