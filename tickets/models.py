from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tickets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)

    resolved = "resolved"
    unresolved = "unresolved"
    freezed = "frezzed"

    statuses = [
        (resolved, 'Resolved'),
        (unresolved, 'Unresolved'),
        (freezed, 'Freezed')
    ]

    status = models.CharField(max_length=16, choices=statuses, default=unresolved)    
    objects = models.Manager()
    
    def __str__(self):
        return self.title