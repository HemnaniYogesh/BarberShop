from django.shortcuts import render, redirect
#from sms import send_sms
# password:- inia sdax xqak nzkb#

from django.core.mail import send_mail
import smtplib
from django.conf import settings
from .models import Inquiry, Blog, About, Portfolio, Hairstyle, Massage, Beardstyle
from .models import Form

from django.http import JsonResponse
import razorpay
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "myapp/index.html")


def about(request):
    data=About.objects.all
    return render(request, "myapp/about.html", {"data":data})


def blog(request):
    data=Blog.objects.all
    return render(request, "myapp/blog.html", {"data":data})



def main(request):
    return render(request, "myapp/main.html")


def portfolio(request):
    data=Portfolio.objects.all
    return render(request, "myapp/portfolio.html",{"data":data})


def services(request):
    return render(request, "myapp/services.html")


# below code to be edited
def contact(request, message=None):

    if request.POST:
        name = request.POST['fname']
        lastname = request.POST['lname']
        phone = request.POST['phone']
        barber1 = request.POST['barber1']
        date1 = request.POST['date1']
        time1 = request.POST['time1']
        email = request.POST['email']
        comment = request.POST['comment']
        obj = Inquiry(name=name, lastname=lastname, phone=phone,barber1=barber1, t_date=date1, t_time=time1, email=email, comment=comment)
        obj.save()
        subject = "Booking an Appointment Wait Until Confirmation Mail"
        message = name+"\n"+lastname+"\n"+phone+"\n"+date1+"\n"+time1+"\n"+comment
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list, False, None, None, None, None)
        return redirect("/#")
    return render(request, "myapp/contact.html")


def stylish_haircut(request):
    data = Hairstyle.objects.all
    return render(request, "myapp/stylish_haircut.html",{"data":data})


def massage(request):
    data = Massage.objects.all
    return render(request, "myapp/massage.html",{"data":data})


def beard_style(request):
    data = Beardstyle.objects.all
    return render(request, "myapp/beard_style.html",{"data":data})


def form(request, message=None):
    if request.POST:
        name=request.POST['fname']
        lastname = request.POST['lname']
        phone1 = request.POST['phone1']
        email = request.POST['email']
        purpose = request.POST['Purpose']
        obj = Form(name=name, lastname=lastname, phone=phone1, email=email,purpose=purpose)
        obj.save()
        subject = "You had requested for Becaming a Member "
        message = name+"\n"+name+"\n"+lastname+"\n"+phone1+"\n"+email+"\n"+purpose
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list, False, None, None, None, None)
        return redirect("/#")
    return render(request, "myapp/form.html")

def membership(request):
    return render(request, "myapp/membership.html")


def payment_process(request):
    # Razorpay KeyId and key Secret
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    amount = int("7000")*100  # Your Amount

    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"BarberShop",
        "notes":{
            'name' : 'YOGESH',
            'payment_for':'BARBERSHOP PROJECT'
        }
    }
    id = request.user.id
    result = 1
    payment = client.order.create(data=data)
    context = {'payment' : payment,'result':result}
    return render(request, 'myapp/payment_process.html',context)

@csrf_exempt
def success(request):
	context = {}
	return render(request,'myapp/success.html',context)

