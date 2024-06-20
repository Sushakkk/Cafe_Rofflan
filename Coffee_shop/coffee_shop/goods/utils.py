from django.db.models import Q
from goods.models import Dishes

def q_search(query):
    
    # query = query.lower()
    # Если запрос состоит только из цифр и его длина не превышает 5 символов
    if query.isdigit() and len(query) <= 5:
        return Dishes.objects.filter(id=int(query))

    # Разделяем запрос на ключевые слова, игнорируя слова длиной 2 и менее символов
    keywords = [word for word in query.split() if len(word) > 2]

    # Создаем объект Q для комплексного поиска
    q_objects = Q()

    # Добавляем условия для поиска по полям description и name без учета регистра
    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    # Выполняем запрос к базе данных с созданными условиями
    return Dishes.objects.filter(q_objects)
