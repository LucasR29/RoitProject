# Roit Automation Project #

# Objective #

### This project was made with the objective of serving as an RPA engineering test for Roit Company ###

The automation will open Google Chrome, access the IBGE page, and collect information from the CNAE list.

The robot will access every section in the selected number of sections, open every first economic activity, and paste
the information in an Excel file, removing accents and special characters.

------------------------------------------------------------------------------------------------------------------------

## Requirements ##

- UI Path Studio
- UI Path Orchestrator connected
- Microsoft Excel
- Google Chrome

## Orchestrator Config -- IMPORTANT ##
### Automation will not work without this ###

1. Go to **Orchestrator** page
2. Click **Assets**
3. Click in the folder **Shared**
4. Click "**Add Assets**"
5. Set Asset name to: **IBGE_URL**
6. Set Asset value to: **https://cnae.ibge.gov.br/?view=estrutura**
7. Click "**Create**"

-----------------------------------------------------------------------------------------------------------------------

## Python Script ##

## Libraries ##

- openpyxl
- unidecode

### What the script does ###

The script will install the required libraries, open the Excel file, remove accents and special characters, set everything to lower case, and save the file.
