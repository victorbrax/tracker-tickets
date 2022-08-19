# Important notes to maintenance:

# python -m venv venv
# .\venv\Scripts\Activate.ps1
# pip3 install pandas pynput openpyxl Jinja2 win10toast tk

# pd.set_option('display.max_columns', None)

# pyinstaller -F --icon=target.ico tracker.pyw

#%% Imports
import os
import pandas as pd
import openpyxl
from openpyxl.styles import PatternFill, Font, colors
from openpyxl.utils import get_column_letter
from tkinter import Tk, filedialog
from pynput.keyboard import Key, Controller
from win10toast import ToastNotifier
from operator import index

#%% Win + D
# It's necessary because the file dialog window appears in the background
keyb = Controller()
keyb.press(Key.cmd)
keyb.press('d')
keyb.release(Key.cmd)
keyb.release('d')

#%% Tkinter Process
root = Tk()
root.withdraw()
#%% Initialize Notification
toaster = ToastNotifier()

#%% File Paths
file_path1 = filedialog.askopenfilename(title='Select the XLSX sheet', initialdir='/Desktop',
                                    filetypes=(("XLSX files .xlsx", "*.xlsx"), 
                                                ("All files", "*.*")))

file_path2 = filedialog.askopenfilename(title='Select the CSV sheet', initialdir='/Desktop',
                                    filetypes=(("CSV files .csv", "*.csv"), 
                                                ("All filess", "*.*")))

file_path3 = filedialog.askdirectory(title='Select the save path', initialdir='/Desktop')

file_path3 = file_path3 + '/Tracker Ninecon.xlsx'

#%% Panda Workers
# Source Readers
df1 = pd.read_excel(file_path1)
df2 = pd.read_csv(file_path2, encoding='UTF-16 LE', sep='	')

#%% Old WHD files restore
backup = pd.ExcelFile(file_path1)
dfbckp1 = pd.read_excel(backup, 'Atuais')
dfbckp2 = pd.read_excel(backup, 'Fechados')

#%% Junk drop 1
df1.drop(['Data de Criação WHD', 'Descrição', 'Comentários'], axis=1, inplace=True) 
df2.drop(['Status', 'Priority', 'Alert Level', 'Tech', 'Location', 
'Request Type', 'Subject', 'Client', 'Updated', 'Unnamed: 13'], axis = 1, inplace = True)

#%% King merge
df3 = df1.merge(df2, left_on='Ticket WHD', right_on='No.', how='left')

#%% Junk drop 2
df3.drop(['No.'], axis = 1, inplace = True)
# New file sobreposition rename
df3.rename(columns={'Notes': 'Comentários', 'Date': 'Data de Criação WHD', 
'Request Detail': 'Descrição'}, inplace=True)

#%% New file ordinate
df3 = df3 [['Ticket 4BIZ', 'Ticket WHD', 'Data de Criação 4Biz', 'Data de Criação WHD',
'Titulo', 'Descrição', 'Modulo', 'Priorização', 'Horas Aptdas', 'Impacto',
'Urgencia', 'Tipo', 'Solicitante', 'Consultor', 'Status', 'Ticket Fornecedor',
'Vencimento SLA', 'Ultima Atualização', 'Data Resolvido', 'Comentários']]

#%% Date format functions
df3['Data de Criação WHD'] = pd.to_datetime(df3['Data de Criação WHD']).dt.strftime('%d/%m/%Y')
df3['Data de Criação 4Biz'] = pd.to_datetime(df3['Data de Criação 4Biz']).dt.strftime('%d/%m/%Y')
df3['Vencimento SLA'] = pd.to_datetime(df3['Vencimento SLA']).dt.strftime('%d/%m/%Y')

#%% Condition save (Messenger)
df3.to_excel(file_path3 , index=False)

#%% Conditional Format
# Yellow rows function
def row_style(row):
    if row['Priorização'] == 'Sim':
            return pd.Series('background-color: yellow', row.index) 
    elif row['Impacto'] == 'Alto':
            return pd.Series('background-color: yellow', row.index) 
    else:
        return pd.Series('', row.index)

df3 = df3.style.apply(row_style, axis=1)

#%% Intern sheets room
# Intern sheets ordinate
writer = pd.ExcelWriter(file_path3, engine='openpyxl')
df3.to_excel(writer, sheet_name='BY TRACKER GENERATOR 2.2', index=False)
dfbckp1.to_excel(writer, sheet_name='Atuais', index=False)
dfbckp2.to_excel(writer, sheet_name='Fechados', index=False)

#%% Sheets ordinate save (Organizer)
writer.save()

# Closers
writer.close()
backup.close()

#%% Header format
# Reader
wb = openpyxl.load_workbook(file_path3) 
ws = wb['BY TRACKER GENERATOR 2.2']
fill_cell = PatternFill(patternType='solid', fgColor='104367')

cell = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
for i in cell:
    ws[i].fill = fill_cell
    ws[i].font = Font(bold=True, color='ffffff', size='12')
    
for idx, col in enumerate(ws.columns, 1):
    ws.column_dimensions[get_column_letter(idx)].auto_size = True

#%% Final save!
wb.save(file_path3)

# Closers
wb.close()

#%% Remove old files
os.remove(file_path1)
os.remove(file_path2)

#%% Sucess notification
toaster.show_toast("We won!", "Tracker generated sucessfully", 
icon_path=r"C:\Users\joaog\OneDrive\Programação\me\Projetos\Python\Tracker\TrackerG 2.1\check.ico", 
duration=30, threaded=True)