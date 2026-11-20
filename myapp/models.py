
from django.db import models


class Employee(models.Model):
    eid = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Employee ID"
    )
    ename = models.CharField(
        max_length=100,
        verbose_name="Full Name"
    )
    eemail = models.EmailField(
        verbose_name="Email Address"
    )
    econtact = models.CharField(
        max_length=15,
        verbose_name="Contact"
    )

    def __str__(self):
        return self.ename
