from django.db import models
from students.models import BaseModelClass

# Create your models here.

class StatusChoices(models.TextChoices):

    PENDING = 'Pending','Pending'

    SUCCESS = 'Sucess','Sucess'

    FAILED = 'Failed','Failed'

class Payments(BaseModelClass):

    student = models.ForeignKey('students.Students',on_delete=models.CASCADE)

    course = models.ForeignKey('course.Course',on_delete=models.CASCADE)

    amount = models.FloatField()

    status = models.CharField(max_length=15,choices=StatusChoices.choices,default=StatusChoices.PENDING)

    paid_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):

        return f'{self.student.name}-{self.course.title}-{self.amount}'
    
    class Meta :

        verbose_name = 'Payments'

        verbose_name_plural = 'Payments'



class Transactions(BaseModelClass):

    payment = models.ForeignKey('Payments',on_delete=models.CASCADE)

    rzp_order_id = models.SlugField(null=True,blank=True)

    status = models.CharField(max_length=15,choices=StatusChoices.choices,default=StatusChoices.PENDING)

    transaction_at = models.DateField(null=True,blank=True)


    def _str_(self):

        return f'{self.payment.student.name}-{self.course.title}-Transaction'
    
    class Meta:
        verbose_name = 'Transaction'

        verbose_name_plural = 'Transactions'