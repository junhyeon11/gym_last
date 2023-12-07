from django.contrib.auth.models import AbstractUser
from django.db import models

class User_information_table(AbstractUser):
    locker = models.BooleanField(default=False)
    lockerpw = models.IntegerField(default=0)
    PT = models.BooleanField(default=False)
    PT_starttime = models.DateTimeField(auto_now=False, null=True, blank=True)
    PT_endtime = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.username  