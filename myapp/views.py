from django.shortcuts import render
from  myapp.models import Worker
def index_page(request):

    all_worker = Worker.objects.all() # Получить все данные из таблицы Worker.
    print(all_worker)

    worker_filtered = Worker.objects.filter(salary=80000) # Получить данные по фильтру.
    print(f'80т.руб. получает: {worker_filtered}')

    for i in all_worker:
        print(f'Фамилия: {i.second_name}, Имя: {i.name}, Зарплата: {i.salary}, Номер: {i.id}')

    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about,html')

