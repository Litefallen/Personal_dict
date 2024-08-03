import json
import keyboard

from to_xls import save_word, open_xlsx_file
from word_search import search_for_word


keyboard.wait('esc')
search_for_word()



# for i in  open_xlsx_file().values:
#     print(i)
