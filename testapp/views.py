from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,newstudent
from .forms import LoginForm
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def view(request):
    return HttpResponse("<h1>Welcome to Django</h1>")
def index(request):
    return render(request,'home.html',{'name':'Irfan'})
def addition(request):
    num1=int(request.POST["val1"])
    num2=int(request.POST["val2"])
    result=num1+num2
    return render(request,'result.html',{'result':result})

def employee(request):
    details=Emp.objects.all()
    return render(request,'home1.html',{'viewdetails':details})


def each_employee(request,id):
    details=Emp.objects.get(id=id)
    return render(request,'home2.html',{'details':details})

def displayform(request):
    form=Student()
    return render(request,'display_form.html',{'form':form})
def formvalidation(request):
    form=Student()
    if request.method == 'POST':
        form=Student(request.POST,request.FILES)
        if form.is_valid():
            name1=form.cleaned_data['name']
            age1=form.cleaned_data['Age']
            address1=form.cleaned_data['Address']
            gender1=form.cleaned_data['gender']
            fav_fruit=form.cleaned_data['favorite_fruit']
            email1=form.cleaned_data['email']
            password1=form.cleaned_data['password']
            con_pwd=form.cleaned_data['Confirmpassword']
            file=form.cleaned_data['fileupload']
            formval=newstudent()
            formval.name=name1
            formval.Age=age1
            formval.Address=address1
            formval.gender=gender1
            formval.favorite_fruit=fav_fruit
            formval.Email=email1
            formval.password=password1
            formval.Confirmpassword=con_pwd
            formval.fileupload=file
            formval.save()
            return HttpResponse("Data saved successfully")
    return render(request,'display_form.html',{'form':form})

def new_stud(request):
    dbdetails=newstudent.objects.all()
    return render(request,'dbdetails.html',{'dbdetails':dbdetails})

def email(request):
    toemail=[('123@gmail.com'),('345@gmail.com'),('abc@yahoo.com')]
    send_mail('subject','message','abcde@gmail.com',toemail,fail_silently=False)
    return HttpResponse('Email sent successfully')
# def newemail(request):
#     email_details=emailnew()
#     return render(request,'emails.html',{'email_details':email_details})
# def emailmethod(request):
#     if request.method=="POST":
#         form=emailnew(request.POST,request.FILES)
#         if form.is_valid():
#             subject=form.cleaned_data['subject']
#             message=form.cleaned_data['message']
#             from_add=form.cleaned_data['from_add']
#             to_add=form.cleaned_data['to_add']
#             attachment=form.cleaned_data['attachment']
#             email=EmailMessage(subject,message,from_add,[to_add])
#             email.attach(attachment.name,attachment.read(),attachment.content_type)
#             email.send()
#             return HttpResponse("<h1>Email Sent Successfully </h1>")
#     else:
#             form=emailnew()
#     return render(request,'emails.html',{'form':form})

def demo_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email_id=form.cleaned_data['mail_id']
            password=form.cleaned_data['password']
            request.session['sessionusername']=username
            return redirect('home3')
    else:
            form=LoginForm()
    return render(request,'login.html',{'form':form})

def home3(request):
    uname=request.session['sessionusername']
    return render(request,'home3.html',{'username':uname})





