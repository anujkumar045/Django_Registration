from django.shortcuts import render,redirect
from .models import Employee
from .models import Department 
from .models import Empquery
from django.contrib import messages
from django.core.mail import send_mail

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
            # user=Employee.objects.filter(Email=e)
            # if not user:
            #     msg="Register First"
            #     return redirect('register')
            # else:
            #     userdata=Employee.objects.get(Email=e)
            #     if p==userdata.Password:
            #         req.session['user_id']=userdata.id
            #         return redirect('userdashboard')
            #     else:
            #         msg='Email & Password not match'
            #         return render(req,'login.html',{'umsg':msg})
            employee=Employee.objects.filter(Email=e)
            if employee:
                emp_data=Employee.objects.get(Email=e)
                if p==emp_data.Code:
                    req.session['emp_id']=emp_data.id
                    print(emp_data.id)
                    print(emp_data.Code)
                    print(p)
                    return redirect('empdashboard')
                else:
                    messages.warning(req,"Email and Passsword does not matched")
                    return redirect('login')
            else:
                messages.warning(req,"Not a registered user")
                return redirect("login")   
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
    else:
        return redirect('login')
    
def add_dep(req):
    if 'a_data' in req.session:
        a_data=req.session.get('a_data')
        return render(req,'admindashboard.html',{'data':a_data,'add_dep':True})
    else:
        return redirect('login')

def save_data(req):
    if 'a_data' in req.session:
        if req.method=='POST':
            d_n=req.POST.get('name') 
            d_c=req.POST.get('code') 
            d_h=req.POST.get('head') 
            d_d=req.POST.get('description')
            dept=Department.objects.filter(Dep_name=d_n)
            if dept:
                messages.warning(req,'Department already exists')
                a_data=req.session.get('a_data')
                return render(req,'admindashboard.html',{'data':a_data,'add_dep':True})
            else:
                Department.objects.create(Dep_name=d_n,Dep_code=d_c,Dep_head=d_h,Dep_description=d_d)
                messages.success(req,"Department created")
                a_data=req.session.get('a_data')
                return render(req,'admindashboard.html',{'data':a_data,'add_dep':True})
    else:
        return redirect('login')

def show_dep(req):
    if 'a_data' in req.session:
        a_data=req.session.get('a_data')
        all_dept=Department.objects.all()
        return render(req,'admindashboard.html',{'data':a_data,'show_dep':True,'all_dept':all_dept})
    else:
        return redirect('login')
    
def add_emp(req):
    if 'a_data' in req.session:
        a_data=req.session.get('a_data')
        all_dept=Department.objects.all()
        return render(req,'admindashboard.html',{'data':a_data,'add_emp':True,'all_dept':all_dept})
    else:
        return redirect('login')

def save_emp(req):
    if 'a_data' in req.session:
        if req.method=='POST':
            e_n=req.POST.get('emp_name') 
            e_c=req.POST.get('emp_contact') 
            e_e=req.POST.get('emp_email') 
            e_d=req.POST.get('emp_dept')
            e_co=req.POST.get('emp_code')
            e_i=req.FILES.get('emp_image')
            emp=Employee.objects.filter(Email=e_e)
            if emp:
                messages.warning(req,'Employee already exists')
                a_data=req.session.get('a_data')
                return render(req,'admindashboard.html',{'data':a_data,'add_emp':True})
            else:
                Employee.objects.create(Name=e_n,Contact=e_c,Email=e_e,Department=e_d,Code=e_co,Image=e_i)
                send_mail(
                        "Mail coming from django server",
                        f'This information regarding your company credential Name:{e_n}, Email:{e_e},Contact:{e_c}, Department={e_d},Code={e_co}',
                        "prasadanujkumar045@gmail.com",
                        [e_e],
                        fail_silently=False,
                        )
                messages.success(req,"Employee added")
                a_data=req.session.get('a_data')
                return render(req,'admindashboard.html',{'data':a_data,'add_dep':True})
    else:
        return redirect('login')
    
def show_emp(req):
    if 'a_data' in req.session:
        a_data=req.session.get('a_data')
        all_emp=Employee.objects.all()
        all_dept=Department.objects.all()
        return render(req,'admindashboard.html',{'data':a_data,'show_emp':True,'all_emp':all_emp,'all_dept':all_dept})
    else:
        return redirect('login')
    
def emp_all_query(req):
    if 'a_data' in req.session:
        a_data=req.session.get('a_data')
        all_query=Empquery.objects.all()
        return render(req,'admindashboard.html',{'data':a_data,'emp_all_query':True,'all_query':all_query})
    else:
        return redirect("login")

def reply(req,pk):
    if 'a_data' in req.session:
        q_data=Empquery.objects.get(id=pk)
        emp_all_query=Empquery.objects.all()
        return render(req,{'q_data':q_data,'emp_all_query':emp_all_query})
    
def empdashboard(req):
    if 'emp_id' in req.session:
        eid=req.session.get('emp_id')
        emp_data=Employee.objects.get(id=eid)
        return render(req,'empdashboard.html',{'data':emp_data})
    else:
        return redirect('login')
    
def query(req):
    if 'emp_id' in req.session:
        # emp_data=req.session.get('emp_id')
        eid=req.session.get('emp_id')
        emp_data=Employee.objects.get(id=eid)
        all_dept=Department.objects.all()
        return render(req,'empdashboard.html',{'data':emp_data,'query':True,'all_dept':all_dept})
    return redirect('empdashboard')

def profile(req):
    if 'emp_id' in req.session:
        # emp_data=req.session.get('emp_id')
        eid=req.session.get('emp_id')
        emp_data=Employee.objects.get(id=eid)
        # all_dept=Department.objects.all()
        return render(req,'empdashboard.html',{'data':emp_data,'profile':True})
    return redirect('empdashboard')

def setting(req):
    if 'emp_id' in req.session:
        # emp_data=req.session.get('emp_id')
        eid=req.session.get('emp_id')
        emp_data=Employee.objects.get(id=eid)
        # all_dept=Department.objects.all()
        return render(req,'empdashboard.html',{'data':emp_data,'setting':True})
    return redirect('empdashboard')

def querydata(req):
    if req.method=='POST':
        if 'emp_id' in req.session:
            n= req.POST.get('name')
            e= req.POST.get('email')
            d= req.POST.get('department')
            q = req.POST.get('query')
            Empquery.objects.create(Name=n,Email=e,Department=d,Query=q)
            messages.success(req,"Query created")
            eid=req.session.get('emp_id')
            emp_data=Employee.objects.get(id=eid)
            all_dept=Department.objects.all()
            return render(req,'empdashboard.html',{'data':emp_data,'query':True,'all_dept':all_dept})
        else:
            return redirect('empdashboard')
    return redirect('login')
    
def all_query(req):
    if 'emp_id' in req.session:
        eid=req.session.get('emp_id')
        emp_data=Employee.objects.get(id=eid)
        all_dept=Department.objects.all()
        all_query=Empquery.objects.filter(Email=emp_data.Email)
        return render(req,'empdashboard.html',{'data':emp_data,'all_query':True,'all_query':all_query,'all_dept':all_dept})
    else:
        return redirect("login")

def pending_query(req):
    if 'emp_id' in req.session:
        eid=req.session.get('emp_id')
        emp_data=Employee.objects.get(id=eid)
        all_dept=Department.objects.all()
        pending_query=Empquery.objects.filter(Status="pending")
        return render(req,'empdashboard.html',{'data':emp_data,'pending_query':True,'all_query':pending_query,'all_dept':all_dept})
    else:
        return redirect("login")
    
def done_query(req):
    if 'emp_id' in req.session:
        eid=req.session.get('emp_id')
        emp_data=Employee.objects.get(id=eid)
        all_dept=Department.objects.all()
        pending_query=Empquery.objects.filter(Status="done")
        return render(req,'empdashboard.html',{'data':emp_data,'done_query':True,'all_query':done_query,'all_dept':all_dept})
    else:
        return redirect("login")

def edit1(req):
    return render(req,'edit.html')

def reset(req):
     if 'emp_id' in req.session:
        if req.method=='POST':
        # emp_data=req.session.get('emp_id')
            eid=req.session.get('emp_id') 
            image=req.FILES.get('img')
            emp_data=Employee.objects.get(id=eid)
            emp_data.Image=image
            emp_data.save()
            messages.success(req,"Image changed successfully")
            return redirect('profile')
        else:
            return render(req,'edit.html')
     return render(req,'login.html')


    
        
        
        
