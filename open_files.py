    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:12:05 2019
@author: pedrocampelo
"""

#bibliotecas importadas
import os
import sys
import pandas as pd
import csv

from xlrd import *
import win32com.client
import sys



#definir o diretório
def input_wd(work_path):
    
    """
    Antes de abrir o arquivo é necessário definir o local de trablalho. 
    Basta colar o o local de trabalho quando chamar a função e ela ajusta as barras (que sao ao contrario no python)
    e define qual o local de trabalho pela biblioteca os. A função tentar mudar o diretório, caso o caminho não seja encontrado, 
    o diretório volta para o inicial.
    Verificar:
    https://www.geeksforgeeks.org/python-os-chdir-method/
    """


    cwd = os.getcwd() 
    print ("Seu diretório de trabalho atual é:", cwd)

    try: 
        cwd = os.chdir(r work_path)
        print("Inserting inside-", os.getcwd()) 

    except: 
        print("Aconteceu algo de erado com o diretório especificado. Exceção:", sys.exc_info()) 
        cwd = os.getcwd()

    # finally: 
    #    print("Restoring the path") 
    #    os.chdir(cwd) 
    #    print("Current directory is-", os.getcwd())     


    print ("O novo diretório de trabalho é:", cwd)

    return cwd
    

#abrir arquivos csv
def open_csv(file_name):
    
    """
    Esta função le arquivos em txt e retorna um dataframe.
    Verificar atributos em:  
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    """

    df = pd.read_csv(file_name, index_col='coluna_indice', sep=';')

    return  df   
    
    
    
#abrir arquivos txt
def open_txt(file_name):
    
    """
    Esta função le arquivos em txt e retorna um dataframe.
    O arquivo txt pode ser lido da mesma forma que o csv, o que vai variar é com a forma da base de dados e 
    como o separador vai ser usado.
    Verificar atributos em:  
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    """

    df = pd.read_csv(file_name, index_col='coluna_indice', sep=',')

    return df




#abrir arquivos xlsx/xsl
def open_excel(file_name, sheet_name):
    
    """
    Esta função le arquivos em excel e retorna um dataframe.
    Verificar atributos em:  
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html ]
    https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython
    """

    df = read_excel(file_name, sheetname=sheet_name, header=0, index_col='coluna_indice')

    return df



#abrir arquivos xslx com senha
def open_excel_passwd(file_path, passwd):
    
    """
    Esta função le arquivos em excel protegido por senha e retorna um dataframe.
    Checar open pyxl.
    Verificar atributos em:  
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html ]
    https://stackoverflow.com/questions/16888888/how-to-read-a-xlsx-file-using-the-pandas-library-in-ipython

    https://openpyxl.readthedocs.io/en/stable/index.html
    """

    import openpyxl
    wb = openpyxl.load_workbook(file_path)
    wb.security.workbookPassword = passwd

    #or try
    xlApp = win32com.client.Dispatch("Excel.Application")
    xlwb = xlApp.Workbooks.Open(file_path, False, True, None, passwd)

    return df


#salvar arquivos
def save_file(df,file_type, path,file_name):
    
    """
    Esta função salvao dataframe em csv ou xlsx como desejar.
    Caso deseje salvar em txt, só mudar o nome do arquivo final salvo em csv para '.txt'.
    Verificar atributos:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter
    """
    if file_type=='csv':
        
        df.to_csv(path+'/'+file_name+'.xlsx', index_col=False, sep=',', encoding='utf-8')
        
        
    if file_type=='xlsx':
        
        #dividindo o dataframe em 2 salvando em duas abas diferentes.
        df1=df1[:10]
        df2=df1[10:]
        
        writer = pd.ExcelWriter(path+file_name+'.xlsx')
        df1.to_excel(writer,'sheet1')
        df2.set_index('index_col')
        df2.to_excel(writer,'sheet1')
        writer.save()

        
if __name__== "__main__":
    
    cwd=input_wd(work_path)
    df=open_csv(file_name)
    df=open_txt(file_name)
    df=open_excel(file_name, sheet_name)
    df=open_excel_passwd(file_path, passwd)
    save_file(df,file_type, path,file_name):
    
    
    
    


