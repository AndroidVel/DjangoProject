from django.shortcuts import render
from django.views.generic import TemplateView


def view_class(request):
    return render(request, 'second_task/class_template.html')


class ViewFunc(TemplateView):
    template_name = 'second_task/func_template.html'
