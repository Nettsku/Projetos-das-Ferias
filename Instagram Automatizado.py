import click
from selenium import webdriver
from senha import senha2
import time

#Uma brincadeira feito pelo Nettsku(Ketsuo) e o Douglas

Navegador = webdriver.Chrome("chromedriver.exe") #Google chorme
Navegador.get("https://www.instagram.com/")  #Instagram
time.sleep(2)
Navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('matheus-coliveira@hotmail.com') #Login
Navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha2) #Senha
Navegador.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click() #Botão de entrar
time.sleep(2)
Navegador.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click() #Não Lembrar senha
time.sleep(2)
Navegador.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click() #Não ter Notificações
time.sleep(1)
Navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]').click() #click Barra de pesquisar
Navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("dougla@almeida123") #Digitando na barra de pesquisar o instagram que queremos
time.sleep(1)
Navegador.find_element_by_class_name('-qQT3').click() #Click no instagram que queremos
time.sleep(0.5)
Navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click() #Seguir

    #Curtindo uma foto do amiguinho :3 (Extras)
Navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[2]').click
Navegador.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]/span/svg').click


