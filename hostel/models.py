from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(AbstractUser):
#     USER_TYPE_CHOICES = ((1, "student"), (2, "admin"))
#     user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

class LeaveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=3000)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    visiting_place = models.CharField(max_length=100)

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=3000)
    expected_time = models.DateTimeField(auto_now_add=True)

class HealthReport(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reporter")
    reportee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reportee")
    description = models.CharField(max_length=3000, null=True)
    date = models.DateTimeField(auto_now_add=True)

class RoomCleaning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)
