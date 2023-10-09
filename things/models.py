from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator


# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False
    )
    description = models.TextField(
        blank=True,
        validators=[
            MaxLengthValidator(
                limit_value=120,
                message="Description cannot be longer than 120 characters."
            )
        ]
    )
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Quantity should be more than or equal to 0."
            ),
            MaxValueValidator(
                limit_value=100,
                message="Quantity should be less than or equal to 100."
            )
        ]
    )
