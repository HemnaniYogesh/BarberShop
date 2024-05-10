'''
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''

from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Barber App Admin"
admin.site.site_title = "Barber App Admin Portal"
admin.site.index_title = "Welcome to Barber App Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about', views.about),
    path('blog', views.blog),
    path('contact', views.contact),
    path('portfolio', views.portfolio),
    path('services', views.services),
    path('portfolio', views.portfolio),
    path('main', views.main),
    path('stylish_haircut', views.stylish_haircut),
    path('massage', views.massage),
    path('beard_style', views.beard_style),
    path('form', views.form),
    path('membership', views.membership),
    path('payment_process', views.payment_process),
    path('success', views.success),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
