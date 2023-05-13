def clean_table():
    from openpyxl import load_workbook

    file = load_workbook("IBGE_STRUCTURE.xlsx")

    sheet = file['Sheet1']

    for row in sheet:
        for cell in row:
                string = cell.value

                print(type(string))

    # file.save("IBGE_STRUCTURE.xlsx")

clean_table()