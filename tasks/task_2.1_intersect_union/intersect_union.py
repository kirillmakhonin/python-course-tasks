from functools import reduce
from operator import contains
#test = [[y for y in range(1,x)] for x in range(4,100)]
    
def intersect(*args):
    '''Вычисляет пересечение множеств удалением невалидных элементов из первого множества '''
    result = list(args[0])
    for collection in args[1:]:
        for item in result[:]:
            if item not in collection:
                result.pop(item)
    return result


def union(*args):
    result = list()
    for collection in args:
        for item in collection:
            if item not in result:
                result.append(item)
    return sorted(result)


# intersect в функциональном виде
intersect_func = lambda *args: [item for item in args[0] if map(lambda collection: item in collection, args[1:])]
