def count_words(s: str) -> int:
  return len(s.split())

def dict_of_chars(s: str) -> dict:
  d = {}
  for char in s.lower():
    if char in d:
      d[char] += 1
    else:
      d[char] = 1
  return d

def dict_to_list(d: dict) -> list:
  l = []
  def get_num(l: list) -> int:
    return l["num"]
  for k in d:
    l.append({"char": k, "num": d[k]})
  l.sort(reverse=True, key=get_num)
  return l