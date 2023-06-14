from django import forms

class TaxCalculatorForm(forms.Form):
    income = forms.DecimalField(label='Ежегодный доход')
    employees = forms.IntegerField(label='Среднее количество сотрудников')
    labor_expenses = forms.DecimalField(label='Расходы на оплату труда')
    other_expenses = forms.DecimalField(label='Иные расходы')
