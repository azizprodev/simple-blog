from django.db import models
from datetime import datetime
# from autoslug import AutoSlugField

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    # slug = AutoSlugField(populate_from = "title", unique=True, null=True, default=None)
