def code(a: str) -> int:
  result = 0
  for char in a:
    o = ord(char)
    while o>0:
      result *= 10
      o = o // 10
    result += ord(char)
  return result

