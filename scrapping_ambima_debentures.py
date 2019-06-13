#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:12:05 2019
@author: pedrocampelo
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup




def set_request(cod_ativo):
    
    """"
    Esta função trás acha o site e verifica se os dados são possiveis de serem extraídos
        Caso seja possível, aparecerá 'Requisição bem sucedida!'.
        Caso contrário, aparecerá 'Falha na requisição'
        
    Além disso, essa função devolve um dataframe bagunçado
    """
    
    req = requests.get('http://www.debentures.com.br/exploreosnd/consultaadados/emissoesdedebentures/caracteristicas_d.asp?tip_deb=publicas&selecao='+cod_ativo)

    if req.status_code == 200:
        print('Requisição bem sucedida!')
        content = req.content
    else:
        print('Falha na requisição')
        
    soup = BeautifulSoup(content, 'html.parser')
    #duas opcoes

    #1 - table retornará uma lista de todas as tabelas
      table = soup.find_all(name='table')

      table_str = str(table)
      df_aux = pd.read_html(table_str)[0]

    #2 - 
      table = soup.find(name='table', attrs={'id':'id_table_body'})

      table_str = str(table)
      df_aux = pd.read_html(table_str)[0]

    return df_aux




def save_df(df, indicador, data):

    """"
    Essa função abre o arquivo xlxs, appenda os novos dados e salva o df
    """    
 
    
#    writer = pd.ExcelWriter('dados_lag'+str(forecastHorizon)+'v2.xlsx')
#    coef_sum_df.to_excel(writer,'coeficientes_lag'+str(forecastHorizon))
#    previsao.set_index('Modelos')
#    previsao.to_excel(writer,'previsao_lag'+str(forecastHorizon))
#    writer.save()
    
    return None



if __name__== "__main__":
  
    
    """"
    Em cima eu desenvolvi todas as funções, aqui em baixo eu rodo cada uma termino o código.
    """"
    
    deb_lista = list(df_ISIN['Cod Ativo']    
    for deb in deb_lista:
       
        df_aux=set_request(data, indicador)
        df=set_dataframe(df_aux, indicador)
        save_df(df, indicador, data)
        
