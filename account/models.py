from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),

)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)
    profile_image = models.ImageField(null=True, blank=True, upload_to="media/images")
    cv = models.FileField(null=True, blank=True, upload_to="media/cv")


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


