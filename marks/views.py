
from django.views.generic import TemplateView
from marks.models import  Student,Marks
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    #students = Student.objects.create(student_number=1,student_name='Nadhia',gender='female',age=23)
    students= Student.objects.all()
    return render(request, 'home.html', {'students': students})
def about_us(request):
    return render(request,'about_us.html')
def my_account(request):
    return render(request,'my_account.html')
def contact(request):
    return  render(request,'contact.html')
class student(TemplateView):
    template_name = 'student.html'
    def get(self,request):
        #students = Student.objects.filter(student_name='Florence Namukwaya')
        students = Student.objects.all()
        args = {'students': students}
        return render(request,self.template_name, args)
class marks(TemplateView):
    template_name = 'marks.html'
    def get(self,request):
        marks = Marks.objects.all()
        args = {'marks': marks}
        return render(request,self.template_name, args)
def student_marks(request, pk):
        marks =Marks.objects.get(pk=pk)
        args = {'marks': marks}
        return render(request, 'marks.html',args)


#class about_us(View):
    #def render(self, request):
       #return render(request, 'about_us.html')



