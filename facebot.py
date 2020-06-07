#!-*- coding: utf8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

login  = 'seu@email.com'
senha  = 'sua_senha'

comment_cont = 1

print("abrindo Chrome")

chrome_path = r"../facebot-master/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(10)

print("logando na conta")

def login_gshow():

    driver.get("https://facebook.com")
    input_login = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input""")
    input_password = driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input""")
    input_login.send_keys(login)
    input_password.send_keys(senha)
    sleep(2)
    driver.find_element_by_xpath("""/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input""").click()
login_gshow()

comment = "ae"

print("abrindo página pra comentar")
sleep(10)

def comentar():

    driver.get("https://www.facebook.com/post_que_quer_comentar")
    sleep(2)
    driver.find_element_by_class_name("""_7c-t""").click()
    driver.find_element_by_xpath("""/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div/div/form/div/div/div[2]/div/div/div/div""").send_keys(comment_cont, Keys.RETURN)

print("comentando")

while(True):
    comentar()
    comment_cont = comment_cont + 1
    print("{} comentários feitos".format(comment_cont))
