from django.db import models
from django.utils import timezone
from django.contrib import admin


class Company(models.Model):
    name = models.CharField(max_length=50)


class Employee(models.Model):
    name = models.CharField(max_length=65)
    position = models.CharField(max_length=50)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(auto_now_add=False, blank=False)
    end_time = models.DateTimeField(auto_now_add=False, blank=False)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
