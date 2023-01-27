from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Place
from . models import People
def demo(request):
    obj=Place.objects.all()
    obj1=People.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj1})

#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res=x+y
    #return render(request,"Result.html",{'result':res})