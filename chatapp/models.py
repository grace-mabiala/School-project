from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Etudiant(models.Model):
    user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    message=models.TextField()


    def __str__(self):
      return self.user.username

    
