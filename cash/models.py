from django.utils import timezone
from django.db import models


class ProofOfTransaction(models.Model):
    proof_file = models.FileField()


class CashFlow(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('debit',  'Debit'),
        ('credit', 'Credit')
    )
    datetime = models.DateTimeField(default=timezone.now)
    transaction_proof = models.ForeignKey(ProofOfTransaction, null=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    transaction_type = models.CharField(
        choices=TRANSACTION_TYPE_CHOICES, default='credit',
        null=False, blank=False, max_length=6
    )
    transaction_value = models.PositiveIntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return "{0}: {1}".format(self.description, self.transaction_value)
