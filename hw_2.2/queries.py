#friends = [
#    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
#    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
#]


def select(*field_names: list):
    '''Формирует функцию которая возвращает набор данных только с переданными полями ?Фабрика?  
    :param field_names: Список полей выводимых в выборке
    :type field_names: list
    '''
    def actual_select(data):
        '''Возвращает набор данных только по указанным полям
        :param data: collection of records
        :type data: iterable
        '''
        # проверка что поле(pair[0]) должно остаться в выборке
        return [{pair for pair in record.items() if pair[0] in field_names} for record in data] 
    return actual_select

def field_filter(field: str, values: list):
    '''Формирует фильтр по полю field с допустимыми значениями values. ?Фабрика?
    :param field: поле для фильтрации
    :type field: str
    :param values: допустимые значения
    :type field: list
    '''
    def actual_filter(data):
        '''Фильтрует набор данных по значениям одного из полей
        :param data: collection of records
        :type data: iterable
        '''
        return filter(lambda record: record[field] in values, data)
    return actual_filter

def query(data: list, select_func, *filters):
    '''Функция применяет фильтры к набору данных и убирает ненужные поля
    :param data: список словарей, начальный набор данных
    :type data: list
    :param select_func: функция отбора полей для вывода
    :type select_func: Callable
    :param filters: фильтры
    :type filters: Callable
    '''
    for func in filters:
        data = func(data)
    return select_func(data)
