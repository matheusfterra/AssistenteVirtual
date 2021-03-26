import pickle
from time import sleep
import datetime, pytz
import random



def default_functions(webdriver, logger):

        #Acessa página
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        # Realiza o download dos cookies
        save_cookies(webdriver,'Cookies/')
        #Pausa Aleatória
        sleep(random.randint(3, 7))
        #Encontra elemento pelo nome
        elemento = webdriver.find_element_by_name('username')
        #Digitação lenta
        slow_type(elemento,"Texto aqui")
        #Encontra elemento pelo xpath
        elemento = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button/div')
        #Data Atual para inserção no banco de dados
        date=formatted_datetime_utc_now()
















#Funções Default
def slow_type(element, text):
    #Pega a mensagem a ser digitada e aplica um sleep em caractere por caractere
    for s in text:
        element.send_keys(s)
        sleep(0.1)


def convert_utc_zone(date):
    #Converte a hora atual para o horario padrao (fuso 0)
    date_time_obj = datetime.datetime.strptime(date.replace('T', ' ').replace('Z', ''), '%Y-%m-%d %H:%M:%S.%f')

    dtobj3 = date_time_obj.replace(tzinfo=pytz.UTC).strftime("%Y-%m-%d %H:%M:%S")  # replace method

    #dtobj_saopaulo = dtobj3.astimezone(pytz.timezone("America/Sao_Paulo")).strftime("%Y-%m-%d %H:%M:%S")  # astimezone method
    date_time_obj_export = datetime.datetime.strptime(dtobj3, '%Y-%m-%d %H:%M:%S')
    return(date_time_obj_export)


def formatted_datetime_utc_now():
    #Prepara a data/hora atual para registro no BD
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    formatted_datetime = utc_now.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_datetime


def save_cookies(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookies(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)



