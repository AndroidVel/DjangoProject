from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

users = []


def fill_inputs(dict_, username, password, repeat_password, age):
    dict_['username'] = username
    dict_['password'] = password
    dict_['repeat_password'] = repeat_password
    dict_['age'] = int(age)


def sign_up_by_html(request):
    info = {'error': ''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            fill_inputs(info, username, password, repeat_password, age)
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            fill_inputs(info, username, password, repeat_password, age)
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            fill_inputs(info, username, password, repeat_password, age)
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {'error': '', 'username': '', 'password': '', 'repeat_password': '', 'age': 0}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        info['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                fill_inputs(info, username, password, repeat_password, age)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                fill_inputs(info, username, password, repeat_password, age)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                fill_inputs(info, username, password, repeat_password, age)
            else:
                users.append(username)
                return HttpResponse(f'Приветствуем, {username}!')
        else:
            form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)
