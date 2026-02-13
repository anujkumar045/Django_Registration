from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    if req.method=='POST':
      n=req.POST.get('name')
      g=req.POST.get('gender')
      q=req.POST.getlist('qualification')
      ag=req.POST.get('age_group')
      e=req.POST.get('email')
      c=req.POST.get('contact')
      p=req.POST.get('password')
      cp=req.POST.get('confirm_password')
      user = Employee.objects.filter(Email=e)
      if user :
          msg="Email id already exists!"
          return render(req,'register.html',{'msg':msg})
      else:
          if p==cp:    
              Employee.objects.create(
              Name=n,
              Gender=g,
              Qualification=q,
              Age_group=ag,
              Email=e,
              Contact=c,
              Password=p,
              Confirm_Password=cp,
              )
              return redirect('login')
          else:
              userdata={'name':n,'email':e,'contact':c}
              msg="Password & Confirm_password not matched"
              return render(req,'register.html',{'pmsg':msg,'data':userdata})
    return render(req,'register.html')


def login(req):
    if req.method=='POST':
        e=req.POST.get('email')
        p=req.POST.get('password')
        if e=='admin@gmail.com' and p=='admin':
            a_data={
                'id':1,
                'name':'Admin',
                'email':'admin@gmail.com',
                'password':'admin'
            }
            req.session['a_data']=a_data
            return redirect('admindashboard')
        else:
            user=Employee.objects.filter(Email=e)
            if not user:
                msg="Register First"
                return redirect('register')
            else:
                userdata=Employee.objects.get(Email=e)
                if p==userdata.Password:
                    req.session['user_id']=userdata.id
                    return redirect('userdashboard')
                else:
                    msg='Email & Password not match'
                    return render(req,'login.html',{'umsg':msg})
    return render(req,'login.html')

def userdashboard(req):
    if 'user_id' in req.session:
        x=req.session.get('user_id')
        userdata=Employee.objects.get(id=x)
        return render(req,'userdashboard.html',{'data':userdata})
    return redirect('login')

def logout(req):
    if 'user_id' in req.session:
        req.session.flush()
        return redirect('login')
    return redirect('login')

def admindashboard(req):
    if 'a_data' in req.session:
        a_data=req.session.get('a_data')
        return render(req,'admindashboard.html',{'data':a_data})