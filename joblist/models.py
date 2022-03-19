from django.db import models
from django.conf import settings
from django.db.models.fields.files import ImageField
from django.core.files.storage import FileSystemStorage
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
        storage=FileSystemStorage(location=settings.JOB_STORAGE),
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

    class Meta:
        ordering = ['-id']
        
    def __str__(self) -> str:
        return f'{self.company} : {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
