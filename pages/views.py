from pages.models import Subject
from django.shortcuts import render
from django.contrib import messages, auth
from .choices import class_of_subjects, editions


# Home page
def index(request):
        return render(request, 'pages/index.html')

# About Page
def about(request):
        return render(request, 'pages/about.html')

# Subjects
def subjects(request):
    queryset = Subject.objects.all()
    #Class_of_subject
    if 'class_of_subject' in request.GET:
        class_of_subject = request.GET['class_of_subject']
        if class_of_subject:
            queryset = queryset.filter(class_of_subject__iexact=class_of_subject)
    #Edition
    if 'edition' in request.GET:
        edition = request.GET['edition']
        if edition:
            queryset = queryset.filter(edition__iexact=edition) 
    #ISBN
    if 'isbn' in request.GET:
        isbn=request.GET['isbn']
        if isbn:
            queryset = queryset.filter(isbn__icontains=isbn) 
    #Subject name
    if 'subject' in request.GET:
        subject=request.GET['subject']
        if subject:
            queryset = queryset.filter(subject__icontains=subject)
    #author
    if 'author' in request.GET:
        author=request.GET['author']
        if author:
            queryset = queryset.filter(author__icontains=author)          
    
    context = {
        'class_of_subjects': class_of_subjects,
        'editions': editions,
        'subjects': queryset,
        'values': request.GET
    }

    return render(request, 'pages/subjects.html', context)

# Online apply page
def online_apply(request):
    return render(request, 'pages/online_apply.html')