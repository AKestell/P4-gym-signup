from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GymClass(models.Model):
    DAYS = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday')
    ]
    
    name = models.CharField(max_length=100)
    day_of_week = models.IntegerField(choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} on {self.get_day_of_week_display()} from {self.start_time} to {self.end_time}"