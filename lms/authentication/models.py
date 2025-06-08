from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoice(models.TextChoices):

    ADMIN = 'Admin' , 'Admin'

    STUDENT = 'Student' , 'Student'

    Instructor = 'Instructor' , 'Instructor'

class Profile(AbstractUser):

    # image = models.ImageField(upload_to='profile-images/')

    role = models.CharField(max_length=15,choices=RoleChoice.choices)

    def __str__(self):

        return f'{self.first_name}-{self.last_name}-{self.role}'
    
    class Meta:

        verbose_name = 'Profile'

        verbose_name_plural = 'Profile'

# Profile.objects.create_user(username='johndoe@mailinator.com',email='johndoe@mailinator.com',first_name='John',last_name='Doe',role='Instructor',password='password123')