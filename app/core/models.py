from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    """creates and saves new user"""
    def create_user(self,email,Password=None,**kwargs):
        if not email:
            raise ValueError("Email cannot be none")
        user = self.model(email=self.normalize_email(email),**kwargs)
        user.set_password(Password)
        user.save(using = self._db) #using = self._db when you have multiple databases
        return user
    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser =  True
        user.save(using = self._db)
        return user
    


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length = 255,unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email' #change username field to email default is usernae