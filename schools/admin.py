from django.contrib import admin
from .models import Applies, Schools, Subject, Teacher, Student, Comment
# Register your models here.
admin.site.register(Schools)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Comment)
admin.site.register(Subject)
admin.site.register(Applies)