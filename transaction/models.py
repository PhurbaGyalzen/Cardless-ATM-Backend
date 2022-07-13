from ssl import Purpose
from django.db import models

class Withdraw(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    account_number = models.CharField(max_length=20)
    account_name = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20)
    account_bank = models.CharField(max_length=20)
    account_branch = models.CharField(max_length=20)
    remarks = models.CharField(max_length=200)
    purpose = models.CharField(max_length=20)
    bank_code = models.CharField(max_length=20)
    atm_code = models.CharField(max_length=20)
    atm_location = models.CharField(max_length=20)

    def __str__(self):
        return str(self.account_number)

    class Meta:
        verbose_name_plural = "Withdraw"
        ordering = ['-date']
        db_table = "withdraw"