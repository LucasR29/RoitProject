import os

os.system('pip install openpyxl')
os.system('pip install unidecode')

from openpyxl import load_workbook
import unidecode 

def clean_table():
    file = load_workbook("IBGE_STRUCTURE.xlsx")

    sheet = file.active

    for row in sheet.iter_rows(min_row=2):
        for cell in row[1:]:
                string = unidecode.unidecode(cell.value).lower()

                cell.value = string

    file.save("IBGE_STRUCTURE.xlsx")

clean_table()