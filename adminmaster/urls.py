"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')')
"""

from django.contrib import admin
from django.urls import path
from adminmaster import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home', views.home),
                  path('', views.login),
                  path('registration1', views.registration),
                  path('member', views.member),
                  path('create_blog', views.create_blog),
                  path('create_portfolio', views.create_portfolio),
                  path('create_about', views.create_about),
                  path('inbox', views.inbox),
                  path('blog', views.blog),
                  path('portfolio', views.portfolio),
                  path('about', views.about),
                  path('confirm', views.confirm),
                  path('add_hairstyle', views.add_hairstyle),
                  path('add_massage', views.add_massage),
                  path('add_beardstyle', views.add_beardstyle),
                  path('stylish_haircut', views.stylish_haircut),
                  path('massage', views.massage),
                  path('beard_style', views.beard_style),
                  path('delete/<int:id>', views.delete),
                  path('remove/<int:id>', views.remove),
                  path('done/<int:id>', views.done),
                  path('logout', views.logout),
                  path('forgetpassword', views.forgetpassword),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
