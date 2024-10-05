from pprint import pprint
import csv
import re
from collections import OrderedDict

with open("phonebook_raw.csv", encoding="utf-8") as f:
  new_phone_book = []
  for line in f:
      last_name, first_name, surname, organization, position, phone, email = line.rstrip().split(",")
      
      # правим фио
      whole_name = last_name, first_name, surname
      other_info = organization, position, phone, email
      whole_name = ' '.join(whole_name)
      name = whole_name.split()
      for i in other_info:
          name.append(i)
          new_line = ', '.join(name)
          
          # правим номер телефона
          phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
          phone_numb_sub = r'+7(\2)\3-\4-\5\7\8\9'
          result = re.sub(phone_pattern, phone_numb_sub, new_line)
          result = result.split(', ')
          
      new_phone_book.append(result)
  
  # объединяем дубли
  k = 0
  while k < len(new_phone_book) - 1:
      for list1, list2 in zip(new_phone_book[k], new_phone_book[k + 1]):
          if list1 == list2:
              new_list = list(OrderedDict.fromkeys(new_phone_book[k] + new_phone_book[k + 1]))
              new_phone_book.remove(new_phone_book[k + 1])
              new_phone_book.remove(new_phone_book[k])
              new_phone_book.append(new_list)
          break
      k += 1
      print(new_phone_book)
    
# пишем в новый файл
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f)
    datawriter.writerows(new_phone_book)
