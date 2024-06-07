from django.db import models

# Create your models here.
# taskmanager/models.py
from django.db import models
import uuid

class ScrapingTask(models.Model):
    job_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    coin = models.CharField(max_length=50)
    output = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
