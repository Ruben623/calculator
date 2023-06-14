from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from models import TaxCalculation
from .forms import TaxCalculatorForm


def determine_tax_regime(income, employees, labor_expenses, other_expenses):
    if income <= 1000000 and employees <= 10 and labor_expenses <= 200000:
        # Рекомендуемый режим налогообложения: УСН "доходы"
        tax_regime = 'УСН "доходы"'

    elif income <= 6000000 and employees <= 100 and labor_expenses <= 1000000 and other_expenses <= 300000:
        # Рекомендуемый режим налогообложения: УСН "доходы-расходы"
        tax_regime = 'УСН "доходы-расходы"'

    elif income <= 15000000 and employees <= 100 and labor_expenses <= 2000000 and other_expenses <= 500000:
        # Рекомендуемый режим налогообложения: ОСНО
        tax_regime = 'ОСНО'

    else:
        # Рекомендуемый режим налогообложения: патент
        tax_regime = 'патент'

    return tax_regime



def calculate_tax(income, employees, labor_expenses, other_expenses, tax_regime):
    if tax_regime == 'ОСНО':
        # Расчет суммы налога для режима ОСНО
        # Ваш код для расчета суммы налога по режиму ОСНО
        taxable_income = income - labor_expenses - other_expenses
        tax_rate = 0.20  # Примерная ставка налога для ОСНО (20%)
        tax_amount = taxable_income * tax_rate  # Рассчитанная сумма налога для ОСНО

    elif tax_regime == 'УСН "доходы"':
        # Расчет суммы налога для режима УСН "доходы"
        # Ваш код для расчета суммы налога по режиму УСН "доходы"
        tax_rate = 0.06  # Примерная ставка налога для УСН "доходы" (6%)
        tax_amount = income * tax_rate  # Рассчитанная сумма налога для УСН "доходы"

    elif tax_regime == 'УСН "доходы-расходы"':
        # Расчет суммы налога для режима УСН "доходы-расходы"
        # Ваш код для расчета суммы налога по режиму УСН "доходы-расходы"
        taxable_income = income - labor_expenses
        tax_rate = 0.05  # Примерная ставка налога для УСН "доходы-расходы" (5%)
        tax_amount = taxable_income * tax_rate  # Рассчитанная сумма налога для УСН "доходы-расходы"

    elif tax_regime == 'патент':
        # Расчет суммы налога для режима "патент"
        # Ваш код для расчета суммы налога для "патент"
        patent_rate = 0.06  # Примерная ставка налога для патента (1 000 000 рублей)
        tax_amount = patent_rate  # Рассчитанная сумма налога для "патент"

    else:
        # Некорректный режим налогообложения
        tax_amount = 0

    return tax_amount


def tax_calculation(request):  # HttpRequest
    if request.method == 'POST':
        form = TaxCalculatorForm(request.POST)
        if form.is_valid():
            income = form.cleaned_data['income']
            employees = form.cleaned_data['employees']
            labor_expenses = form.cleaned_data['labor_expenses']
            other_expenses = form.cleaned_data['other_expenses']

            # Выполнить расчеты для определения рекомендуемого режима налогообложения и суммы налога

            # Рекомендуемый режим налогообложения
            tax_regime = determine_tax_regime(income, employees, labor_expenses, other_expenses)

            # Расчет суммы налога
            tax_amount = calculate_tax(income, employees, labor_expenses, other_expenses, tax_regime)

            # Сохранение результатов расчета в базе данных
            tax_calculation = TaxCalculation(
                income=income,
                employees=employees,
                labor_expenses=labor_expenses,
                other_expenses=other_expenses,
                tax_regime=tax_regime,
                tax_amount=tax_amount
            )
            tax_calculation.save()

            # Вернуть результаты расчета налогов в шаблон для отображения
            context = {
                'tax_regime': tax_regime,
                'tax_amount': tax_amount
            }
            return render(request, 'result.html', context)
    else:
        form = TaxCalculatorForm()

    context = {
        'form': form
    }
    return render(request, 'tax_calculator.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h4>')

