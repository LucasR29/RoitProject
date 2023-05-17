import os

os.system('pip install openpyxl')
os.system('pip install unidecode')

import openpyxl
import unidecode

def clear_table(path):
    file = openpyxl.load_workbook(path)

    sheet = file.active

    for row in sheet.iter_rows(min_row=2):
        for cell in row[1:]:
                string = unidecode.unidecode(cell.value).lower()

                cell.value = string

    file.save(path)
    
    return "Formatting Completed"