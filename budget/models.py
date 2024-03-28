from django.db import models
from django.utils import timezone

# Create your models here.
class Transaction(models.Model):
    TYPE_CHOICES = (
        ("Income", "Income"),
        ("Expense", "Expense"),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    note = models.TextField(blank=True)
