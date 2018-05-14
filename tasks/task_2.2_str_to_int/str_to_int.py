def str_to_int(a: str) -> int:
    '''Перевод строки в число без приведения типов'''
    result = 0
    for char in a:
        num = ord(char)
        while num>0:
        result *= 10
        num = num // 10
        result += ord(char)
    return result

