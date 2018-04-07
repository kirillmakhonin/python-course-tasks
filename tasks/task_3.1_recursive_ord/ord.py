#!/usr/bin/env python3
def code_recursive(string: str) -> int:
    """Transforms string into number with sybols' UTF codes
    
    :param str string: string to transform
    :rtype: int
    """
    if not string:
        return 0
    num = ord(string[-1])
    num_len = 0
    while num > 0:
        num_len += 1
        num = num // 10
    return code_recursive(string[:-1])*10**num_len + ord(string[-1])
    
    
