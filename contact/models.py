from django.db import models

# Create your models here.

STATUS_CHOICES = (
    # When a new customer inquire hasn't been addressed yet
    ('OPEN', 'Open'),
    # When an admin is currently addressing it
    ('IN_PROGRESS', 'In Progress'),
    # When the inquiry has been dealt with and issue is closed
    ('CLOSED', 'Closed'),
)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
