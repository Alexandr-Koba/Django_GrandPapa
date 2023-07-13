from django.shortcuts import render
from  myapp.models import Worker
def index_page(request):

    text = 'Высший пилотаж самые вкустные десерты на острове ко Панган'

    all_worker = Worker.objects.all() # Получить все данные из таблицы Worker.



    return render(request, 'index.html', context={'data': all_worker, 'time': '4:03', 'text': text})

def about_page(request):
    return render(request, 'about,html')

