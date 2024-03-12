from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Membership(models.Model):
    full_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.full_name
    

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, username_field):
        return self.get(**{self.model.USERNAME_FIELD: username_field})

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=16)
    profile_picture = models.ImageField(
    upload_to='profile_pics/', null=True, blank=True)
    membership = models.ForeignKey(Membership, blank=True, null=True, on_delete=models.SET_NULL)
    # add your own
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    detail = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    pass





class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.patient_name