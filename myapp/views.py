from django.shortcuts import render
from  myapp.models import Worker
def index_page(request):

    # ЗАПИСЬ НОВОГО ОБЬЕКТА В БД:
    #new_worker = Worker(name='Алексей', second_name='Путин', salary=350000)
    #new_worker.save()
    '''
    в одну строку
    Worker.objects.create(name='Алексей', second_name='Путин', salary=350000)
    '''

    #worker_to_change = Worker.objects.get(id=5)
    #worker_to_change.salary = 400000
    #worker_to_change.save()
    '''
    в одну строку: Worker.objects.filter(id=5).update(name='Дима')
    '''

    #Worker.objects.get(id=5).delete()

    all_worker = Worker.objects.all() # Получить все данные из таблицы Worker.

    worker_filtered = Worker.objects.filter(salary=80000) # Получить данные по фильтру.
    print(f'80т.руб. получает: {worker_filtered}')

    for i in all_worker:
        print(f'Фамилия: {i.second_name}, Имя: {i.name}, Зарплата: {i.salary}, Номер: {i.id}')

    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about,html')

