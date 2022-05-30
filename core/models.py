from django.db import models


# Create your models here.


class user(models.Model):
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    temp_password = models.CharField(max_length=255)
    isadmin = models.BooleanField(default=False)


class attendance_info(models.Model):
    userAtendance = models.ForeignKey(user, on_delete=models.CASCADE)
    in_time = models.DateTimeField()
    out_time = models.DateTimeField()
    total_duration = models.IntegerField()


class task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
