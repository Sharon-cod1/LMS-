from django.db import models

from course.models import BaseModelClass

# Create your models here.

class QualificationChoices(models.TextChoices):

    MARTRICULATION = 'Matriculation' , 'Matriculation'
    POST_MATRICULATION = 'Post Matriculation' , 'Post Matriculation'
    DIPLOMA = 'Diploma' , 'Diploma'
    GRADUATE = 'Graduate' , 'Graduate'
    POST_GRADUATE = 'Post Graduate' , 'Post Graduate'
    PHD = 'PhD' , 'PhD'
    OTHER = 'Other' , 'Other'

class Students(BaseModelClass):

    profile = models.ForeignKey('authentication.profile',on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='student-images/')

    qualification = models.CharField(max_length=50,choices=QualificationChoices.choices)

    def __str__(self):

        return self.name
    
    class Meta:
        
        verbose_name = 'Students'
        verbose_name_plural = 'Students'