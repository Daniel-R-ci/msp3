from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    """
    Event- Information about upcoming evens
    """
    title = models.CharField(max_length=150)
    content = models.TextField
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    event_date = models.DateField
    event_time = models.TimeField
    public_event = models.BooleanField(default=True)
