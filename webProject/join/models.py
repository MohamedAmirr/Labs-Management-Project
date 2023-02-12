from django.db import models


# Create your models here.


class SignUp(models.Model):
    firstName = models.CharField(max_length=30, null=False, default='firstName')
    lastName = models.CharField(max_length=30, null=False, default='lastName')
    email = models.CharField(max_length=50, null=False, default='email')
    password = models.CharField(max_length=50, null=False, default='password1')

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name = 'costumer'
