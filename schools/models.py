
from django.db import models
from django.db.models.base import Model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE

from accounts.models import User

# Create your models here.
class Schools(models.Model):
    schoolname = models.CharField(max_length=60)
    region = models.CharField(max_length=3, null=True)
    school_type = models.CharField(max_length=3, null=True)
    schoolnumber = models.IntegerField()
    adress = models.CharField(max_length=70)
    teachersnumber = models.IntegerField()
    pupilsnumber = models.IntegerField()
    website = models.CharField(max_length=100, unique=True)
    photo_main = models.ImageField( blank=True)
    photo_1=models.ImageField( blank=True)
    photo_2=models.ImageField( blank=True)
    photo_3=models.ImageField( blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.schoolnumber)

class Teacher(models.Model):
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE, verbose_name="School of Teacher")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 50)
    role = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    ranking = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    image = models.ImageField(upload_to='teachers/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return str(self.first_name)

class Student(models.Model):
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE, verbose_name="School of Student")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 50)
    achievments = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.first_name)

class Subject(models.Model):
    teacher_id = models.ManyToManyField(Teacher, related_name='teacher')
    student_id = models.ManyToManyField(Student, related_name='student')
    subject_name = models.CharField(max_length=50)
    subject_credit = models.IntegerField()
    
    def __str__(self):
        return self.subject_name

class Comment(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Comments for teacher")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    comment = models.TextField()
    hidden = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.comment)

class Applies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField(unique=False)
    body = models.TextField()
    region = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    image = models.ImageField(upload_to='applicants/%Y/%m/%d', blank=True)
    status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)]) 
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    received_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return str(self.first_name)