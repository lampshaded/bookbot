import sys
from stats import count_words, dict_of_chars, dict_to_list

def get_book_text(path: str) -> str:
  with open(path) as f:
    contents = f.read()
    return contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
  
  path = sys.argv[1]

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  frank_text = get_book_text(path)

  print("----------- Word Count ----------")
  frank_num_words = count_words(frank_text)
  print(f"Found {frank_num_words} total words")

  print("--------- Character Count -------")
  frank_dict_chars = dict_of_chars(frank_text)
  frank_list_chars = dict_to_list(frank_dict_chars)
  for d in frank_list_chars:
    if d["char"].isalpha():
      print(f"{d['char']}: {d['num']}")
  
  print("============= END ===============")


main()