from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords


class Todo(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='todos'
    )
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    history = HistoricalRecords()
    
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title
# Create your models here.
