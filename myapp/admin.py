from django.contrib import admin
from myapp.models import Blog, About, Portfolio, Hairstyle, Massage, Beardstyle

# Register your models here.

admin.site.register(Blog)

admin.site.register(About)

admin.site.register(Portfolio)

admin.site.register(Hairstyle)

admin.site.register(Massage)

admin.site.register(Beardstyle)
