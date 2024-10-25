from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'fourth_task/main_page.html'


class Shop(TemplateView):
    template_name = 'fourth_task/shop.html'


class Cart(TemplateView):
    template_name = 'fourth_task/cart.html'
