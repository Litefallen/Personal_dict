import keyboard
from word_search import search_for_word
from testing import skillcheck, choose_num
from to_xls import get_all_words, open_xlsx_file


workbook = open_xlsx_file()
while True:
    print('Press "shift+right" to start the app.')
    keyboard.wait('shift+right')  # waking up an app with a hotkey. Change it to the shortcut you prefer
    print('1. Add word', '2. Test yourself', '3. See all words')
    choice = choose_num([1, 2, 3])
    if choice == 0:
        search_for_word(workbook)
        continue

    if choice == 1:
        rounds = 5  # amount of the words in a test
        skillcheck(rounds, workbook)
        continue

    if choice == 2:
        print('*Only the shortest meaning of the word is displayed here.')
        all_words = get_all_words(workbook)
        if not all_words:
            print('Sorry, no words were found..')
        else:
            for word in all_words:
                print(word[0], end='. ')
                print(word[1], word[2], word[3], sep='--')
        continue
