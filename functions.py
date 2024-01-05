import requests
from bs4 import BeautifulSoup
import os
from consts import *


def init():
    os.system("cls")
    print("### Start")
    while True:
        try:
            process()
        except:
            process()


def separator(separator_alt=""):
    sep = "----------------------------------------------------------------------------------------"
    if separator_alt != "":
        sep = sep.replace("-", separator_alt)
    print(sep)


def get_data_ticker(ticker):
    url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontre as informações que você deseja na página
        preco_fechamento = soup.find('td', {'data-test': 'OPEN-value'}).text
        volume_negociado = soup.find('td', {'data-test': 'TD_VOLUME-value'}).text

        return {
            'Ticker': ticker,
            'Preço de Fechamento': preco_fechamento,
            'Volume Negociado': volume_negociado
        }
    else:
        separator()
        print(f"Não foi possível obter dados para o ticker {ticker}")
        return None


def get_data_ticker_list():
    for ticker in CST_TICKERS:
        list_ticker(ticker)


def list_ticker(ticker=''):
    if ticker.strip() != '':
        data_ticker = get_data_ticker(ticker)        
        if data_ticker:
            separator()
            for key, value in data_ticker.items():
                print(f"-> {key}: {value}")
    else:
        get_data_ticker_list()


def process():
    separator()
    print("TICKER PROGRAM")
    separator()
    print("Option below:")
    print()
    print("\t1 - List tickers;")
    print("\t2 - Input ticker;")
    print("\t3 - List suggestion;")
    print("\t4 - Exit.")
 
    option = int(input("\nChoose? ")[:1])
    
    if option == 1:
        list_ticker()
    elif option == 2:
        ticker = input("> Type the ticker (like: AAPL para Apple): ")
        list_ticker(ticker)
    elif option == 3:
        print("> List of ticker suggestion:")
        for ticker in CST_TICKERS:
            print(ticker)        
    else: 
        exit()


def end():
    print()
    print("### End")