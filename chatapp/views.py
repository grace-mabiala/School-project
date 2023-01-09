from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import Etudiant
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('message')
        else:
            errors="vous vous etes pas inscris dans notre chatbox"
            return render(request,'chatapp/home.html',{"errors":errors})
           

    return render(request,'chatapp/home.html',{})



def message(request):
    return render(request,'chatapp/message.html',{})



#la methode pour s'occuper de l'enregistrement
def register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

        else:

            return render(request,'chatapp/registration.html',{'form':form})   
    return render(request,'chatapp/registration.html',{'form':form})  





@login_required(redirect_field_name='home')
def message_box(request):
    etudiants=Etudiant.objects.all()
    username=str(request.user.username)
    if request.method=='POST':
        message=request.POST['message']
        Etudiant.objects.create(user=request.user,message=message)
        return render(request,'chatapp/chat.html',{'etudiants':etudiants,"username":username})
    return render(request,'chatapp/chat.html',
    {'etudiants':etudiants})   

def logout_view(request):
    logout(request,request.user)
       

def deletemessage(request,id):

    etudiants=Etudiant.objects.get(pk=id)
    etudiants.delete()
    etudiants=Etudiant.objects.all()
    return redirect('message_box')     