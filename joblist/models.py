from distutils.command.upload import upload
from django.db import models
from django.db.models.fields.files import ImageField
from utils.genslug import gen_slug
from utils.uploadimg import upload_job_img
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


# Create your models here.

class JobCategory(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class JobCompany(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class JobCard(models.Model):
    slug = models.SlugField(blank=True, editable=False)
    created_date = models.DateField(default=timezone.now(),blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    category = models.ForeignKey(JobCategory,on_delete=models.CASCADE,blank=True,null=True,related_name='category_jobs')
    company = models.ForeignKey(JobCompany,on_delete=models.CASCADE,blank=True,null=True,related_name='company_jobs')
    logo = ImageField(
        upload_to=upload_job_img,
        blank=True,
        null=True
    ) 
    location = models.CharField(max_length=200,blank=True,null=True)
    job_type = models.CharField(max_length=200,blank=True,null=True)
    deadline = models.DateField(blank=True,null=True)
    experience = models.CharField(max_length=200,blank=True,null=True)
    description = RichTextUploadingField(blank=True,null=True)
    contact = models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        ordering = ['-id']
        
    def __str__(self) -> str:
        return f'{self.company} : {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
