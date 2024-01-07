from django.contrib import admin
from .models import Instructor, Login, Register, Category, Course, Testimonial

# Register your models here.
# admin.site.register(Instructor)
# class Instructor():
#     list_display=("name", )

admin.site.register(Register)
class Register():
    list_display=('first_name',)    

admin.site.register(Login)
class Login():
    list_display=('user',)

admin.site.register(Category)
class Category():
    list_display=('name',)

admin.site.register(Course)
class Course():
    list_display=('title',)

admin.site.register(Testimonial)
class Testimonial():
    list_display=('name',)

admin.site.register(Instructor)
class Instructor():
    list_display=('name',)