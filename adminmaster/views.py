from django.shortcuts import render, redirect
from myapp.models import Inquiry, Blog, Form, About,Portfolio, Hairstyle, Massage, Beardstyle
from adminmaster.models import Barber, Confirmation, Staff
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def home(request):
    data=Confirmation.objects.all
    return render(request, "adminmaster/home.html", {"data":data})

def registration(request):
    data = Staff.objects.all
    if request.POST:
        u=request.POST['username']
        e=request.POST['email']
        p=request.POST['password']
        obj=Barber(uname=u,email=e,password=p)
        obj.save()
        return redirect('/#')
    return render(request, 'adminmaster/registration.html',{"data":data})

def login(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        count=Barber.objects.filter(email=email,password=password).count()
        if count>0:
            request.session['is_login']=True
            request.session['user_id']=Barber.objects.values('id').filter(email=email,password=password)[0]['id']
            return redirect('/home')
    return render(request,'adminmaster/login.html')


def inbox(request):
    data = Inquiry.objects.all
    return render(request, 'adminmaster/inbox.html',{"data":data})


def member(request):
    data = Form.objects.all
    return render(request, 'adminmaster/member.html',{"data":data})

def create_blog(request):
    return render(request, "adminmaster/create_blog.html")


def blog(request):
    data = Blog.objects.all
    if request.POST:
        description = request.POST['description']
        img = request.FILES['img']
        obj= Blog(img=img,description=description)
        obj.save()
        return redirect("/home")
    return render(request, "adminmaster/create_blog.html",{"data":data})


def create_portfolio(request):
    return render(request, "adminmaster/create_portfolio.html")

def portfolio(request):
    data = Portfolio.objects.all
    if request.POST:
        img = request.FILES['img']
        obj= Portfolio(img=img)
        obj.save()
        return redirect("/create_portfolio")
    return render(request, "adminmaster/create_portfolio.html",{"data":data})

def create_about(request):
    return render(request, "adminmaster/create_about.html")

def about(request):
    data = About.objects.all
    if request.POST:
        detail = request.POST['detail']
        designation = request.POST['designation']
        img = request.FILES['img']
        obj= About(img=img,detail=detail,designation=designation)
        obj.save()
        return redirect("/create_about")
    return render(request, "adminmaster/create_about.html",{"data":data})

def add_hairstyle(request):
    return render(request,"adminmaster/add_hairstyle.html")

def stylish_haircut(request):
    if request.POST:
        hairstyle = request.POST['hairstyle']
        price = request.POST['price']
        obj=Hairstyle(hairstyle=hairstyle,price=price)
        obj.save()
        return redirect("/add_hairstyle")
    return render(request, "myapp/stylish_haircut.html")


def add_massage(request):
    return render(request,"adminmaster/add_massage.html")

def massage(request):
    if request.POST:
        massage = request.POST['massage']
        price = request.POST['price']
        obj=Massage(massage=massage,price=price)
        obj.save()
        return redirect("/add_massage")
    return render(request, "myapp/massage.html")

def add_beardstyle(request):
    return render(request,"adminmaster/add_beardstyle.html")

def beard_style(request):
    if request.POST:
        beardstyle = request.POST['beardstyle']
        price = request.POST['price']
        obj=Beardstyle(beardstyle=beardstyle,price=price)
        obj.save()
        return redirect("/add_beardstyle")
    return render(request, "myapp/beard_style.html")


def confirm(request, message=None):
    if request.POST:
        name = request.POST['fname']
        lastname = request.POST['lname']
        phone = request.POST['phone']
        barber1 = request.POST['barber1']
        date1 = request.POST['date1']
        time1 = request.POST['time1']
        email = request.POST['email']
        comment = request.POST['comment']
        obj = Confirmation(name=name, lastname=lastname, phone=phone, barber1=barber1, t_date=date1, t_time=time1, email=email, comment=comment)
        obj.save()
        subject = "Confirming an Appointment"
        message = name+"\n"+lastname+"\n"+phone+"\n"+date1+"\n"+time1+"\n"+comment
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list, False, None, None, None, None)
        return redirect('/home')
    return render(request, "adminmaster/confirm.html")


def delete(request,id):
    Inquiry.objects.get(id=id).delete()
    return redirect('/inbox')

def remove(request,id):
    Form.objects.get(id=id).delete()
    return redirect('/member')

def done(request,id):
    Confirmation.objects.get(id=id).delete()
    return redirect('/home')

def logout(request):
    del request.session['is_login']
    return redirect('/#')

def forgetpassword(request):
    if request.POST:
        e=request.POST['email']
        count=Staff.objects.filter(email=e).count()
        data=Staff.objects.get(email=e)
        print(data.password)
        print(count)
        if count > 0:
            subject = 'Forgot Password'
            message = 'Your Password is : '+data.password
            email_from =settings.EMAIL_HOST_USER
            recipient_list = [e]
            send_mail(subject,message,email_from,recipient_list)
            return redirect('/#')
    return render(request,"adminmaster/forgetpassword.html")
