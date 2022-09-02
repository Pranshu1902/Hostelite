from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LeaveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=3000)
    start_date = models.DateField()
    end_date = models.DateField()
    visiting_place = models.CharField(max_length=100)

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=3000)
    expected_time = models.DateTimeField()

class HealthReport(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reportee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

class RoomCleaning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField()
