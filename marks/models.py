from __future__ import unicode_literals
from django.db import models
#from django.db.models import
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Student(models.Model):
    student_number = models.IntegerField('student_number',unique=True,db_index=True)
    student_name = models.CharField('student_name',max_length=200, default='')
    gender = models.CharField('gender',max_length=20,default='')
    age = models.IntegerField('age',default='')

    def __str__(self):
        return self.student_name

class Marks(models.Model):
    student_number =models.ForeignKey(Student,related_name='students',on_delete=models.CASCADE)
    #student_number = models.IntegerField('student_number', unique=True, db_index=True)
    math = models.IntegerField('math',  default='')
    english = models.IntegerField('english', default='')
    agric= models.IntegerField('agric',  default='')
    bio= models.IntegerField('bio',  default='')

class Myaccount(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description =models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
   # image = models.ImageField(upload_to='profile_image',blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Myaccount.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
