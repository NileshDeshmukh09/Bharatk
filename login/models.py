from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_num = models.CharField(max_length=15)

    def __str__(self):
        return "User: "+self.user.username + "Mobile no: "+self.mobile_num