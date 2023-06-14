from django.db import models

class TaxCalculation(models.Model):
    income = models.DecimalField(max_digits=10, decimal_places=2)
    employees = models.PositiveIntegerField()
    labor_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    other_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    tax_regime = models.CharField(max_length=20)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
