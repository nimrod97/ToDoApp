from django.db import models
from datetime import datetime,timedelta
# Create your models here.
class todo(models.Model):
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
    created_at= datetime.now();