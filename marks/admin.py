from django.contrib import admin
from .models import Student, Marks
admin.site.register(Student)
admin.site.register(Marks)
admin.site.site_header ='Administration'
