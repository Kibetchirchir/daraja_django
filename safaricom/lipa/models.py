from django.db import models


class Transaction(models.Model):
    name = models.CharField(max_length=21)
    phone_number = models.IntegerField()
    amount = models.IntegerField()
    tracking_no = models.CharField(max_length=26)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']
