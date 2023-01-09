from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Etudiant



class RegisterForm(ModelForm):
    class Meta:
        model=User
        fields=('username','password')




class EtudiantForm(ModelForm):
    class Meta:
        model=Etudiant
        fields=('user','message')