from django.contrib import admin
from django.urls import path

from calculator.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tax_calculation/', tax_calculation, name=tax_calculation)
]

handler404 = pageNotFound