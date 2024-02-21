from django.db import models

from users.models import User


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        abstract = True


class SplitType(models.IntegerChoices):
    EQUAL = 0, "EQUAL"
    UNEQUAL = 1, "UNEQUAL"
    PERCENTAGE = 2, "PERCENTAGE"


class OwePaymentStatus(models.IntegerChoices):
    PENDING = 0, "PENDING"
    COMPLETE = 1, "COMPLETE"


class Payment(BaseModel):
    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    split_type = models.IntegerField(default=SplitType.EQUAL, choices=SplitType.choices)


class UserOwePayment(BaseModel):
    user_paid = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE, related_name="user_paid")
    user_owe = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE, related_name="user_owe")
    payment = models.ForeignKey(Payment, blank=False, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    status = models.IntegerField(default=OwePaymentStatus.PENDING, choices=OwePaymentStatus.choices)
