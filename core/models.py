from datetime import datetime
from django.db import models


# Create your models here.


class user(models.Model):
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    temp_password = models.CharField(max_length=255)
    isadmin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"


class attendance_info(models.Model):
    userAtendance = models.ForeignKey(user, on_delete=models.CASCADE)
    in_time = models.DateTimeField(default=datetime.now())
    out_time = models.DateTimeField(blank=True, null=True)
    total_duration = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.userAtendance}"


class task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"
