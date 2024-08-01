import deepl
import dotenv
import os
import requests


dotenv.load_dotenv()

def search_for_word(word:str):
    api_key = os.environ.get('API_KEY')
    translator = deepl.Translator(api_key)
    word_definitions = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').json()
    word_definitions = word_definitions[0]['meanings'][0]['definitions']
    if len(word_definitions) >1:
        print('There are multiple definitions of the word...')
        print('Please choose a definition to be stored: ')
        for definition in enumerate(word_definitions, start=1):
            print(definition[0], definition[1]['definition'])
        desired_def = choose_num(word_definitions)
        def_to_store = (word_definitions[desired_def]['definition'])
    else:
        def_to_store = definition[0]['definition']
    word_translation = str(translator.translate_text(f'{word}',target_lang="RU", source_lang='EN',context=def_to_store)) 
    print(word_translation)
    return (word, def_to_store, word_translation)


