from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage
from utils.genslug import gen_slug

# Create your models here.

class Article(models.Model):
    slug = models.SlugField(blank=True, editable=False)
    title = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.title} : {self.date}'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class ArticleFile(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    file = models.FileField(
        storage=FileSystemStorage(location=settings.BLOG_STORAGE)
    )

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,blank=True,null=True,related_name="comments")
    name = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='r_replies')
    main_parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')

    class Meta:
        ordering = ['date']

    def __str__(self) -> str:
        return self.name

