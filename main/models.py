from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    keep_signed_in = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories')
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=20)
    rating = models.IntegerField()
    reviews = models.IntegerField()
    image = models.ImageField(upload_to='courses')
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    rating = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials')
    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    image = models.ImageField(upload_to='instructors')
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='articles')
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.title