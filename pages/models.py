from django.db import models
from django.db.models.fields import IntegerField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Subject(models.Model):
    class_of_subject = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])
    subject = models.CharField(max_length=50)
    author = models.CharField(max_length= 100)
    isbn = models.IntegerField()
    edition = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])
    photo = models.ImageField(upload_to='subjects/%Y/%m/%d', blank=True)
    file = models.FileField(upload_to='subjects/%Y/%m/%d', blank=False)
    def __str__(self):
        return self.subject