from django.shortcuts import render
from django.http import HttpResponse
from .models import Instructor, Login, Register, Category, Course, Testimonial
from django.views.generic import ListView

def main(request):
    return render(request, 'index.html')

