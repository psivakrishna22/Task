from django.shortcuts import render
from .models import Signup

# Create your views here.
def signup(request):
    if request.method == "POST":
        name=request.POST['name']
        dob=request.POST['dob']
        email=request.POST['email']
        number=request.POST['number']
        gender=request.POST['gender']
        flatno=request.POST['flatno']
        street=request.POST['street']
        country=request.POST['country']
        image=request.POST['image']
        s=Signup(name=name,dob=dob,email=email,number=number,gender=gender,flatno=flatno,street=street,country=country,image=image).save()
        print(s)
    return render(request, 'home.html',{'success':'successfully uploaded'})