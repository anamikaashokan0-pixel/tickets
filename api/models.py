from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=12,unique=True)


class Ticket(models.Model):

    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    CATEGORY_CHOICES=[
        ("TECHNICAL","TECHNICAL"),
        ("PAYMENT","PAYMENT"),
        ("ACCOUNT","ACCOUNT"),
        ("DELIVERY","DELIVERY"),
        ("PRODUCT","PRODUCT"),
        ("OTHER","OTHER")
    ]
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=200)
    PRIORITY_CHOICES=[
        ("LOW","LOW"),
        (" MEDIUM"," MEDIUM"),
        ("HIGH","HIGH"),
        ("URGENT","URGENT")
    ]
    priority=models.CharField(choices=PRIORITY_CHOICES,max_length=200)
    STATUS_CHOICES=[
        ("OPEN","OPEN"),
        ("IN_PROGRESS","IN_PROGRESS"),
        ("RESOLVED","RESOLVED"),
        ("CLOSED","CLOSED")
    ]
    status=models.CharField(choices=STATUS_CHOICES,max_length=200)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ticket")
    assigned_to = models.ForeignKey(User,on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='assigned_tickets')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title