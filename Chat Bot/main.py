from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


navegador = webdriver.Chrome()

navegador.get('https://web.whatsapp.com/')

while True:
    while len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')) < 1:
        pass
    
    while len(navegador.find_elements(By.ID,'side')) < 1:
        pass

    noti = navegador.find_elements(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[12]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span')

    msg = navegador.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[14]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span')

    while True:
        if len(noti) >0:
            msg[0].click()
            input_msg = navegador.find_element(By.CLASS_NAME,'_ak1l')
            input_msg.send_keys("Teste de chat bot enviado com sucesso")
            input_msg.send_keys(Keys.RETURN)
            break
        else:
            pass
    


