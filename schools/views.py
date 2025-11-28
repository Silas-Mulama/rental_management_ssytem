from django.shortcuts import render,get_object_or_404
from schools.models import School,Apartment
# Create your views here.
def Home(request):
    all_sch = School.objects.all()
    return render(request,'schools/all_schools.html',{'schools':all_sch})

def add_school(request):
    return render(request,'schools/add_school.html')

def apartment(request,pk):
    school = get_object_or_404(School,id=pk)
    aprt = Apartment.objects.filter(sch = school)
    
    return render(request,'schools/apartments.html',{'school':school,'apartments':aprt})