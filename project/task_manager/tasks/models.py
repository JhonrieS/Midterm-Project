from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Overdue', 'Overdue'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def save(self, *args, **kwargs):
        """Auto-update status based on due date."""
        if self.due_date and self.due_date < date.today():
            self.status = 'Overdue'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
