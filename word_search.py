import deepl
import dotenv
import os
import requests
from to_xls import save_word
from testing import choose_num

dotenv.load_dotenv() 
api_key = os.environ.get('API_KEY') # get api key from dotenv file
translator = deepl.Translator(api_key)


def search_for_word(workbook):
    workbook = workbook
    word_to_find = input('Please, type the word you want to search for: ').strip()
    word_definitions = requests.get(# get the meaning of the word
        f'https://api.dictionaryapi.dev/api/v2/entries/en/{word_to_find}').json()
    if isinstance(word_definitions, dict):
        print('No definitions found for the word. Please, check the word for typos.')
        return search_for_word(workbook)
    word_definitions = word_definitions[0]['meanings'][0]['definitions']
    word_meanings = [i['definition'].strip() for i in word_definitions][:3] # get only 3 word meanings
    print(f'Here are meanings of the "{word_to_find}" word: ')
    for meaning in word_meanings:
        print(f'- {meaning}')
    word_meanings = ';'.join(word_meanings)
    # option to provide expression using the word to better translation for deepl api
    context = input(f'Please provide example of the expression using the { 
                    word_to_find} word for more precise transtlation OR press "enter" to skip this. ')
    if context:
        word_translation = str(translator.translate_text(
            f'{word_to_find}', target_lang="RU", source_lang='EN', context=context))
    else:
        word_translation = str(translator.translate_text(f'{word_to_find}', target_lang="RU", source_lang='EN'))
    print(f"This is the translation of the word {
          word_to_find}: {word_translation}")
    save_word((word_to_find, word_meanings, word_translation),workbook)
    print('The word was saved.')