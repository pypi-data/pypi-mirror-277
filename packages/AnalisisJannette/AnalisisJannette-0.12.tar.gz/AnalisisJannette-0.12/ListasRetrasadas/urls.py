#configuracion de las urls

from django.urls import path
from .views import IndexView

urlpatternsListasRetrasadas = [
    path('', IndexView.as_view(), name='index'),


]