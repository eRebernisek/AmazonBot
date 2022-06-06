import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlsxwriter

# Configura o Selenium no ambiente Windows para utilizar o Firefox
firefox = webdriver.Firefox(
    executable_path='./geckodriver.exe')


def openBrowser():
    # Abre o site da Amazon no Firefox
    firefox.get('https://amazon.com')
    firefox.maximize_window()

    time.sleep(1)

    # Realiza busca
    firefox.find_element_by_id("twotabsearchtextbox").send_keys('Iphone')
    firefox.find_element_by_id("twotabsearchtextbox").send_keys(Keys.RETURN)


def readValues():
    itemList = firefox.find_elements_by_css_selector(
        'div.s-result-item.s-asin')

    itens = []

    # Formata Valores
    for item in itemList:
        nome = item.find_element_by_class_name('a-text-normal').text
        try:
            inteiro = item.find_element_by_class_name('a-price-whole').text
            fracao = item.find_element_by_class_name('a-price-fraction').text
        except:
            inteiro = '00'
            fracao = '00'
        preco = '$'+str(inteiro)+'.'+str(fracao)

        url = item.find_element_by_class_name(
            'a-link-normal').get_attribute('href')

        itens.append({'nome': nome, 'preco': preco, 'url': url})

    createSheet(itens)


def createSheet(itens):
    livroPlanilha = xlsxwriter.Workbook('Precos_Amazon.xlsx')
    planilha = livroPlanilha.add_worksheet('Iphone')

    planilha.write('A1', 'Produto')
    planilha.write('B1', 'Preço')
    planilha.write('C1', 'Url')

    rowIndex = 2
    for item in itens:
        planilha.write('A'+str(rowIndex), item['nome'])
        planilha.write('B'+str(rowIndex), item['preco'])
        planilha.write('C'+str(rowIndex), item['url'])
        rowIndex += 1

    livroPlanilha.close()


if __name__ == '__main__':
    os.system('clear')
    openBrowser()

    time.sleep(3)
    readValues()

    firefox.close()
    quit()
