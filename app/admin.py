from django.contrib import admin
from .models import MYUSER,Doctor,Patient,Appointment

# Register your models here.
admin.site.register(MYUSER)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)