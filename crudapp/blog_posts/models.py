from django.db import models


# Create your models here.
class UserApis(models.Model):
    name = models.CharField(unique=False, max_length=30)
    email = models.EmailField(unique=True)
    contact = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name
