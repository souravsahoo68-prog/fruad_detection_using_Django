
from django.db import models

class Transaction(models.Model):
    transaction_id = models.BigIntegerField(primary_key=True)
    customer_id = models.IntegerField(db_index=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    location = models.CharField(max_length=100)
    merchant = models.CharField(max_length=200, blank=True, null=True)
    channel = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Txn {self.transaction_id} - {self.customer_id} - {self.amount}"
