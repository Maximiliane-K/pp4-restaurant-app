from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    num_people = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.date_time}'
