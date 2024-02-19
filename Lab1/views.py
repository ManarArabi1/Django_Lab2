from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Student, User

def home(request):
    students=Student.objects.all()
    context={}
    context['students']=students
    return render(request,'Lab1/home.html',context)

def contact(request):
    return render(request, 'Lab1/contact.html')

def about(request):
    return render(request, 'Lab1/about.html')

def student(request):
    students=Student.objects.all()
    context={}
    context['students']=students
    return render(request,'Lab1/home.html',context)

def delete_student(request,id):
    Student.objects.get(id=id).delete()
    return redirect('student')

def signup(request):
    if request.method=='GET':
        return render(request,'Lab1/signup.html')

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['psw']
        name=request.POST['name']
        val=User.objects.filter(email=email)
        if val:
         context = {
                'error_message': "Invalid email pleas try again"
            }
         return render(request,'Lab1/signup.html',context)
           
        User.objects.create(email=email,password=password,name=name)

        return redirect('student')

def signin(request) :
    if request.method == 'GET':
        
        return render(request,'Lab1/login.html')
    
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['psw']
        
        val=User.objects.filter(email=email,password=password)
        
        if val:
            return redirect("student")
        else:
            context={'error_message':'Incorrect email or password'}
            return render(request,'student/login.html' ,context)
   
def create(request) :
    if request.method=='GET':
        return render(request,'Lab1/add_student.html')

    if request.method=='POST':
        id=request.POST['id']
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        age=request.POST['age']
        
           
        Student.objects.create(id=id, f_name=f_name, l_name=l_name, age=age)

        return redirect('student')     
    
def update(request,id) :
    student=Student.objects.get(id=id)
    context={}
    context['students']=student 
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        
        
        student.f_name = fname
        student.l_name = lname
        student.age = age
        student.save()
        return redirect('student')
    return render(request,'Lab1/update_student.html',context)