import keyboard
from word_search import search_for_word
from testing import skillcheck, choose_num
from to_xls import get_all_words


# add choice to remove meanings?
# add option to choose the destination of the file?
# add option to show file path?
# add files merge? or cloud save?

keyboard.add_hotkey('ctrl+shift+right',print, args=(''))
while True:
    print('Press "ctrl+shift+right" to start the app.')
    keyboard.wait('ctrl+shift+right') # waking up an app with a hotkey
    print('1. Add word', '2. Test yourself', '3. See all words')
    choice = choose_num([1,2,3])
    if choice == 0:
        search_for_word()
        continue

    if choice == 1:
        skillcheck(2) # add input for amount of rounds
        continue

    if choice == 2:
        print('*Only the shortest meaning of the word is displayed here.')
        all_words = get_all_words()
        if not all_words:
            print('Sorry, no words were found..')
        else:
            for word in all_words:
                print(word[0],end='. ')
                print(word[1],word[2],word[3], sep='--')
        continue

    

