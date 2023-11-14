from django.shortcuts import render,redirect
from .models import Register,Login
from django.http import HttpResponse


# Create your views here.
def display(request):
    return render(request,'index.html')

def register(request):
     if request.method == 'POST':
         username = request.POST['Username']
         email=request.POST['Email']
         password =request.POST['Password']
         data=Register.objects.create(username=username,email=email,password=password)
         data.save()
         data1=Login.objects.create(email=email,password=password)
         data1.save()
         return redirect(login)






def login(reqeust):
    if reqeust.method == 'POST':
        email = reqeust.POST['Email']
        password = reqeust.POST['Password']
        try:
            data = Login.objects.get( email=email)
            if data.password==password:
                reqeust.session['id']=data.id
                return redirect(home)
            else:
                return HttpResponse("password error")
        except Exception:
            return HttpResponse("USERNAME ERROR")
    else:
        return render(reqeust,'login.html')

def home(request):
    if 'id' in request.session:
        user=request.session['id']
        data=Register.objects.get(id=user)
        context={
            'data':data
        }
        return render(request,'home.html',context)