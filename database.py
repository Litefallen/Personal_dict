import sqlite3

engine = sqlite3.connect('aaa.db')
cursor = engine.cursor()

def create_table(name):
    cursor.execute(f"""create table {name}(
                word TEXT(50),
                word_definition TEXT(150),
                word_translation TEXT(50)
                )""")

def add_word(values:tuple):
    cursor.execute("""INSERT INTO words VALUES(?,?,?)""",values)
    engine.commit()

def get_word(word:str):
    word = cursor.execute(f"""SELECT * FROM words WHERE word == '{word}' LIMIT 1""")
    return word.fetchall()

def get_all_words():
    words = cursor.execute(f"""SELECT * FROM words""")
    return words.fetchall()