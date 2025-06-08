from django.db import models

import uuid

# Create your models here.


class Categorychoice(models.TextChoices):

#    variable = 'value','representation'

    IT_SOFTWARE = 'IT & Software', 'IT & Software'

    FINANCE = 'Finance', 'Finance'

    MARKETING = 'Marketing', 'Marketing'

    IT_SEQURITY = 'IT & Security', 'IT & Security'

class BaseModelClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True

class Levelchoice(models.TextChoices):

    BEGINNER = 'Beginner', 'Beginner'

    INTERMEDIATE = 'Intermediate', 'Intermediate'

    ADVANCED = 'Advanced', 'Advanced'

class Typechoice(models.TextChoices):

    FREE = 'Free', 'Free'

    PREMIUM = 'Premium', 'Premium'
    
class Course(BaseModelClass):

    title = models.CharField(max_length=50)   

    description = models.TextField()

    image = models.ImageField(upload_to='course-images/')

    instructor = models.ForeignKey('instructors.Instructors', on_delete=models.CASCADE)
                                #    app_name.model_name

    category = models.CharField(max_length=25,choices=Categorychoice.choices)

    type = models.CharField(max_length=15,choices=Typechoice.choices)

    tags = models.TextField()

    level = models.CharField(max_length=25,choices= Levelchoice.choices)

    fee = models.DecimalField(max_digits=8, decimal_places=2)

    offer_fee = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)


    def _str_(self):
        return f'{self.title} - {self.instructor}'
    
    class Meta:

        verbose_name = 'Courses'

        verbose_name_plural = 'Courses'

        ordering = ['id']