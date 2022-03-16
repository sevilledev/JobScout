from django.db import models
from django.conf import settings
from django.db.models.fields.files import ImageField
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} : {self.subject}'

class Slider(models.Model):
    image = ImageField(
        storage=FileSystemStorage(location=settings.SLIDER_STORAGE),
        blank=True,
        null=True
    )

    def __str__(self) :
        return f'{self.id}'

class About(models.Model):
    image = ImageField(
        storage=FileSystemStorage(location=settings.SLIDER_STORAGE),
        blank=True,
        null=True
    )
    content = models.TextField()

    def __str__(self) -> str:
        return 'About'

class Service(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name