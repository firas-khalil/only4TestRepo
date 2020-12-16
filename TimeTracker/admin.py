from django.contrib import admin
from .models import Employee, Company, Post

admin.site.register(Post)
admin.site.register(Employee)
admin.site.register(Company)
