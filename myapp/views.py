from django.shortcuts import render
from .models import*
# Create your views here.
def index(request):
    msg='USER CREATED'
    if request.method=='POST':
        User.objects.create(name=request.POST['name'],lastname=request.POST['lastname'],country=request.POST['country'])
        many = User.objects.all()
        return render(request,'index.html',{'msg':msg,'many':many})
    many = User.objects.all()


    return render(request,'index.html',{'many':many})


def delete(request,pk):
    uid=User.objects.get(id=pk)
    uid.delete()
    return render(request,'index.html',{'uid':uid})

def edit(request,pk):
    uid=User.objects.get(id=pk)
    if request.method =='POST':
        uid.name=request.POST['name']
        uid.lastname=request.POST['lastname']
        uid.country=request.POST['country']
        uid.save()
        return render(request,'index.html')


  
    return render(request,'edit.html',{'uid':uid})
    
def search(request):
    

