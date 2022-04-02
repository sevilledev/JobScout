from django.db import models
from django.db.models.signals import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .utils import get_client_ip
from .signals import object_viewd_signal

# Create your models here.

class ObjectViewedQuerySet(models.query.QuerySet):
    def by_model(self,model_class,model_queryset=False):
        c_type = ContentType.objects.get_for_model(model_class,model_queryset=model_queryset)
        qs = self.filter(content_type=c_type)
        if model_queryset:
            viewd_ids = [x.object_id for x in qs]
            return model_class.objects.filter(pk__in=viewd_ids)
        return qs


class ObjectViewedManager(models.Manager):
    def get_queryset(self):
        return ObjectViewedQuerySet(self.model, using=self._db)

    def by_model(self,model_class,model_queryset=False):
        self.get_queryset().by_model(model_class,model_queryset=model_queryset)


class ObjectViewed(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    ip_address = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ObjectViewedManager()

    def __str__(self):
        return str(self.id)
    

def object_viewd_reciver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    obj = ObjectViewed.objects.filter(object_id=instance.id).filter(ip_address=get_client_ip(request)).count()
    print(obj)
    if obj==0:
        new_view_obj = ObjectViewed.objects.create(
            object_id=instance.id,
            content_type=c_type,
            ip_address=get_client_ip(request)
        )

object_viewd_signal.connect(object_viewd_reciver, dispatch_uid=['instance','request'])