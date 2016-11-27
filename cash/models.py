from datetime import datetime

from django.db import models


class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = (
        ('credit', 'Credit'),
        ('debit', 'Debit')
    )
    description = models.CharField(max_length=255, null=False, blank=False)
    value = models.PositiveIntegerField()
    activity_type = models.CharField(choices=ACTIVITY_TYPE_CHOICES, default='credit', max_length=6)
    time = models.DateTimeField(default=datetime.now)
