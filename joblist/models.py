from hashlib import blake2b
from statistics import mode
from django.db import models
from django.conf import settings
from django.db.models.fields.files import ImageField
from django.core.files.storage import FileSystemStorage
from django.forms import CharField
from utils.uploadjobimg import upload_job_img
from utils.genslug import gen_slug

# Create your models here.

class JobCategory(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class JobCard(models.Model):
    slug = models.SlugField(blank=True, editable=False)
    title = models.CharField(max_length=200,blank=True,null=True)
    category = models.ForeignKey(JobCategory,on_delete=models.CASCADE,blank=True,null=True,related_name='jobs')
    logo = ImageField(
        upload_to=upload_job_img,
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        blank=True,
        null=True
    )
    company = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    job_type = models.CharField(max_length=200,blank=True,null=True)
    deadline = models.DateField(blank=True,null=True)
    experience = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    contact = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.company} : {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
