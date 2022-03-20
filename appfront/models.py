from distutils.command.upload import upload
from django.db import models
from django.db.models.fields.files import ImageField
from utils.uploadimg import upload_appfront_img, upload_contact_file
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    message = models.TextField()
    file = models.FileField(
        upload_to=upload_contact_file,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.name} : {self.subject}'

class Slider(models.Model):
    image = ImageField(
        upload_to=upload_appfront_img,
        blank=True,
        null=True
    )

    def __str__(self) :
        return f'{self.id}'

class About(models.Model):
    image = ImageField(
        upload_to=upload_appfront_img,
        blank=True,
        null=True
    )
    content = models.TextField()

    def __str__(self) -> str:
        return 'About'

class Service(models.Model):
    icon_name = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name