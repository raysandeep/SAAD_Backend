from django.db import models
import uuid
# Create your models here.
class operation(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4)
    doctor = models.CharField(max_length=10)
    log = models.TextField(default='')
    important_points = models.CharField(max_length=1000,default='')
    medications = models.TextField(default='')
    operation_time = models.DateTimeField(auto_now_add=True)
    report = models.FileField(default=False)
