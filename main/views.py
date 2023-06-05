from django.shortcuts import render

def index(request):
    # Логика вашего контроллера

    # Возвращение рендера шаблона
    return render(request, 'my_template.html')

