from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Physician(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Physicians"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    license_number = models.CharField(max_length=20)
    specialty = models.ForeignKey(Physician, related_name="doctors", on_delete=models.CASCADE)
    years_of_experience = models.PositiveIntegerField()

    bio = models.CharField(max_length=100)
    clinic_address = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.TextField("M/F")

    description_of_sickness = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, related_name="post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title