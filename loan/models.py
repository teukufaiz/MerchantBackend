from django.db import models

from authentication.models import User

class loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class repayment(models.Model):
    repayment_id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey(loan, on_delete=models.CASCADE)
    amount = models.FloatField()
    repayment_date = models.DateTimeField(auto_now_add=True)