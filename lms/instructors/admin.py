from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Instructors)

admin.site.register(models.AreaOfExpertise)