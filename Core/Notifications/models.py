from django.db import models

# Create your models here.
class Sender(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Notification(models.Model):
    CHANNEL_OPTIONS = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('push', 'Push'),
    ]
    title = models.CharField(max_length=200)
    message = models.TextField()
    channel = models.CharField(
        max_length = 20,
        choices=CHANNEL_OPTIONS
        )

    sender = models.ForeignKey(Sender, on_delete=models.CASCADE, related_name='notifications')

    def __str__(self):
        return self.title