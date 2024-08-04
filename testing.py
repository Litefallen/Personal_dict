from random import randint
from to_xls import open_xlsx_file
all_words = open_xlsx_file()['Dictionary']
all_words = [i[1:] for i in all_words.values][1:]
# print(all_words)
def choose_num(values_list):
    choose_number = input('Please type the corresponding number: ')
    if not choose_number.isdigit() or int(choose_number)-1 not in range(len(values_list)) :
        print('The number you provided is invalid..')
        return choose_num(values_list)
    else:
        return int(choose_number)-1


def select_values(words_list:tuple, word_to_test, test_type:str,  options_amount:int=0):
    if options_amount:
        final_list = [words_list[randint(0, len(words_list)-1)] for _ in range(options_amount)]
        final_list.append(word_to_test)
        final_list = list(set(final_list))
    else:
        final_list = words_list
    if test_type =='translation_ru':
        return list(enumerate([i[2] for i in final_list], start=1))
    if test_type =='translation_en':
        return list(enumerate([i[0] for i in final_list], start=1))
    if test_type =='meaning_en':
        return  list(enumerate([i[1] for i in final_list], start=1))
        

def skillcheck(rounds:int):
    for _ in range(rounds):
        for i in enumerate(('Show english word;', 'show meaning of the word;', 'show russian translation.'),start=1):
            print(f"{i[0]}: {i[1]}", end=' ')
        print()
        test_by = choose_num([1,2,3])
        random_word = all_words[randint(0,len(all_words)-1)]
        if test_by==0:
            print(random_word[0])
            translation_list = select_values(all_words,random_word,'translation_ru',options_amount=3)
            for i in translation_list:
                print(i[0], i[1])
            chosen_var = int(input(f'Please choose the correct translation for "{random_word[0]}" word: ')) -1
            if translation_list[chosen_var][1] == random_word[2]:
                print('You are right! Good job!')
            else:
                print('Wrong!', f'The correct answer is {random_word[2]}')
        if test_by==1:
            print(random_word[1])
            translation_list = select_values(all_words,random_word,'translation_ru',options_amount=3)
            for i in translation_list:
                print(i[0], i[1])
            chosen_var = int(input(f'Please choose the correct translation for the meaning of the {random_word[0]} word: ')) -1
            print(random_word[2],translation_list[chosen_var][1])
            if translation_list[chosen_var][1] == random_word[2]:
                print('You are right! Good job!')
            else:
                print('Wrong!', f'The correct answer is {random_word[2]}')
        if test_by==2:
            print(random_word[2])
            translation_list = select_values(all_words,random_word,'translation_en',options_amount=3)
            for i in translation_list:
                print(i[0], i[1])
            chosen_var = int(input(f'Please choose the correct translation for "{random_word[2]}" word: ')) -1
            if translation_list[chosen_var][1] == random_word[0]:
                print('You are right! Good job!')
            else:
                print('Wrong!', f'The correct answer is {random_word[0]}')
