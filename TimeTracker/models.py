from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=50)


class Employee(models.Model):
    name = models.CharField(max_length=65)
    position = models.CharField(max_length=50)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(auto_now_add=True, blank=True)
    end_time = models.DateTimeField(auto_now_add=True, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

