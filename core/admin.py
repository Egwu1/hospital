from django.contrib import admin

from .models import Doctor, Physician, Patient

# Register your models here.
admin.site.register(Physician)
admin.site.register(Doctor)
admin.site.register(Patient)


