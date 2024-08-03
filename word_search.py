import deepl
import dotenv
import os
import requests
import json


dotenv.load_dotenv()
def search_for_word():
    word_to_find = input('Please, type the word: ')
    api_key = os.environ.get('API_KEY')
    translator = deepl.Translator(api_key)
    word_definitions = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word_to_find}').json()
    if isinstance(word_definitions, dict):
        print('No definitions found for the word. Please, check the word for typos.')
        return search_for_word()
    word_definitions = word_definitions[0]['meanings'][0]['definitions']
    word_meanings = [i['definition'] for i in word_definitions][:3]
    print(f'Here are meanings of the "{word_to_find}" word: ')
    for meaning in word_meanings:
        print('\t- '+meaning)
    word_meanings = ';'.join(word_meanings)
    # context = input(f'Please provide example of the expression using the {word} word for more precise transtlation. Press "enter" to skip.')
    # if context:
    #     word_translation = str(translator.translate_text(f'{word}',target_lang="RU", source_lang='EN',context=context))
    # else:
    #     word_translation = str(translator.translate_text(f'{word}',target_lang="RU", source_lang='EN'))
    # print(word_translation)
    # save_word((word, word_meanings, word_translation))