from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login
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
            error="vous vous etes pas inscris dans notre chatbox"
            return render(request,'chatapp/home.html',{"error":error})
           

    return render(request,'chatapp/home.html',{})



def message(request):
    return render(request,'chatapp/message.html',{})

