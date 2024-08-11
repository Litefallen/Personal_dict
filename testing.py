from random import randint


def choose_num(values_list):
    choose_number = input('Please type the corresponding number: ')
    if not choose_number or not choose_number.isdigit() or int(choose_number)-1 not in range(len(values_list)):  # errorcheck if we get a number
        print('The number you provided is invalid..')
        return choose_num(values_list)
    else:
        return int(choose_number)-1


def get_options(initial_list: list, options_list: list = [], options_amount=4):
    from random import randint, shuffle
    initial_list = initial_list
    if len(options_list) == options_amount:
        shuffle(options_list)  # shuffle options
        return options_list
    else:
        popped_val = initial_list[randint(
            0, len(initial_list)-1)]  # get random word
        options_list.append(popped_val)  # add it to the final options list
        # remove from itinial word list to not to 'pull' it again with randint
        initial_list.remove(popped_val)
        return get_options(initial_list, options_list, options_amount=options_amount)


# for word testing get random options to choose from
def select_values(words_list: list, word_to_test, test_type: str):
    options_amount = o_a if (o_a:= len(words_list)) < 4 else 4 # make sure there wont be errors if amount of words in dictionary is less than 4
    # make sure initial list with words wont become empty with each round of testing
    words_list = list(words_list)
    # remove current testing word from the list...
    words_list.remove(word_to_test)
    # ...and add it to the final options list
    final_list = get_options(initial_list=words_list,
                             options_list=[word_to_test,],options_amount=options_amount)
    if test_type == 'translation_ru':  # return translations or meanings or eng words
        return list(enumerate([i[2] for i in final_list], start=1))
    if test_type == 'translation_en':
        return list(enumerate([i[0] for i in final_list], start=1))
  

def skillcheck(rounds: int, workbook):  # rounds - amount of words in test
    all_words = workbook['Dictionary']
    all_words = [i[1:] for i in all_words.values][1:]
    for _ in range(rounds):
        for i in enumerate(('Show english word;', 'show meaning of the word;', 'show russian translation.'), start=1):
            print(f"{i[0]}. {i[1]}", end='   ')
        print()
        test_by = choose_num([1, 2, 3])
        # get the random word from the list
        random_word = all_words[randint(0, len(all_words)-1)]
        if test_by == 0:
            print(random_word[0])
            translation_list = select_values(
                # get different translations for the word to choose from
                all_words, random_word, 'translation_ru')
            for i in translation_list:
                print(f"{i[0]}. {i[1]}", end='   ')
            print()

            chosen_var = int(input(f'Please choose the correct translation for "{
                             random_word[0]}" word: ')) - 1
            if translation_list[chosen_var][1] == random_word[2]:
                print('You are right! Good job!')
            else:
                print('Wrong!', f'The correct answer is {random_word[2]}')
        if test_by == 1:
            for meaning in random_word[1].split(';'):  # print all the meanings
                print(f"- {meaning}")
            translation_list = select_values(
                # get different translations for the word to choose from
                all_words, random_word, 'translation_ru')
            for i in translation_list:
                print(f"{i[0]}. {i[1]}", end='   ')
            print()
            chosen_var = int(
                input(f'Please choose the correct translation for the meanings above: ')) - 1
            if translation_list[chosen_var][1] == random_word[2]:
                print('You are right! Good job!')
            else:
                print('Wrong!', f'The correct answer is {random_word[2]}')
        if test_by == 2:
            print(random_word[2])  # show russian translation
            translation_list = select_values(
                # get english words to chooce from
                all_words, random_word, 'translation_en')
            for i in translation_list:
                print(f"{i[0]}. {i[1]}", end='   ')
            print()
            chosen_var = int(input(f'Please choose the correct english translation for "{
                             random_word[2]}" word: ')) - 1
            if translation_list[chosen_var][1] == random_word[0]:
                print('You are right! Good job!')
            else:
                print('Wrong!', f'The correct answer is {random_word[0]}')
