from openpyxl import Workbook,load_workbook
def open_xlsx_file():
    try:
        wb = load_workbook('dictionary.xlsx')
    except FileNotFoundError:
        print('No file found')
        wb = Workbook()
        wb.save('dictionary.xlsx')
    try:
        ws = wb['Dictionary']
    except KeyError:
        print('No "Dictionary" sheet found')
        ws = wb.active
        ws.title = 'Dictionary'

        ws['A1'] = 'word_number'
        ws['B1'] = 'english_word'
        ws['C1'] = 'word_meaning'
        ws['D1'] = 'russian_translation'
        wb.save('dictionary.xlsx')
    # print(type(ws.max_row))
    dictionary_workbook = ws
    # print(ws.max_row)
    return dictionary_workbook

open_xlsx_file()


def save_word(word_m_t:tuple):
    wb = open_xlsx_file()
    ws = wb['Dictionary']
    max_row = ws.max_row
    #save initial word, meaning and translation to cells
    ws[f'A{max_row+1}'] = max_row
    ws[f'B{max_row+1}'] = word_m_t[0]
    ws[f'C{max_row+1}'] = word_m_t[1]
    ws[f'D{max_row+1}'] = word_m_t[2]
    wb.save('dictionary.xlsx')

# save_word(('english initial word','meaning of the word', 'translation of the word'))






# wb.save('dictionary.xlsx')