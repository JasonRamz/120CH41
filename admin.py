from django.contrib import admin
from .models import User, Membership,Service,Category,Appointment
# Register your models here.

admin.site.register(User)
admin.site.register(Membership)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Appointment)