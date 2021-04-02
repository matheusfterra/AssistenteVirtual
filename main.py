import sys
import os
from datetime import datetime
import logging

from DBConnectors.Constants import get_agent
from AssistentEngine import AssistentEngine

import undetected_chromedriver as uc


def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('[%(asctime)s] - %(levelname)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)


def init_webdriver(logger):
    AGENT =  get_agent(logger)
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument(f"user-agent= {AGENT}")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--user-data-dir=./Configs/User_Data')
    #chrome_options.add_argument('headless')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    browserdriver = uc.Chrome(
        options=chrome_options
    )

    return browserdriver


def cria_assistente(logger):
    t0_total = datetime.now()
    # Inicia o browser
    browserdriver = init_webdriver(logger=logger)
    # Cria objeto assistente
    assistente = AssistentEngine(browserdriver)
    assistente.whatsapp_agent(logger)

    # Fechamento do browser
    browserdriver.close()
    browserdriver.quit()

    t1_total = datetime.now() - t0_total
    logger.info("Elapsed Total Time: {}\n\n".format(t1_total))





#Cria os diretórios essenciais, caso não existam
if 'Logs' not in os.listdir():
    os.makedirs('Logs')

if 'whatsapp_agent' not in os.listdir('Logs/'):
    os.makedirs('Logs/whatsapp_agent')

if 'telegram_agent' not in os.listdir('Logs/'):
    os.makedirs('Logs/telegram_agent')


#Execução por argumentos na linha de comando.
# try:
#     intention=sys.argv[1]
#
#         #Chama a função de acordo com o argumento da execução do software
#     if intention=="whatsapp_agent":
#         setup_logger('whatsapp_agent', 'Logs/whatsapp_agent/{}.log'.format(datetime.now().strftime('%Y-%m-%d')))
#         logger_whatsapp_agent = logging.getLogger('whatsapp_agent')
#         logger_whatsapp_agent.info("\nIniciando Agente do WhatsApp.")
#         cria_assistente(logger_whatsapp_agent)
#
#     elif intention=="telegram_agent":
#         setup_logger('telegram_agent', 'Logs/telegram_agent/{}.log'.format(datetime.now().strftime('%Y-%m-%d')))
#         logger_telegram_agent= logging.getLogger('telegram_agent')
#         logger_telegram_agent.info("\nIniciando postagem de publicações.")
#         cria_assistente(logger_telegram_agent)
#
#     else:
#         print("Houve um erro na execução do Assistente. Por favor insira um argumento:\n")
#         print("Para execuçãodo Agente do WhatsApp: python main.py whatsapp_agent")
#         print("Para execuçãodo Agente do Telegram: python main.py telegram_agent")
#
# except:
#     print("Houve um erro na execução do Assistente. Por favor insira um argumento:\n")
#     print("Para execuçãodo Agente do WhatsApp: python main.py whatsapp_agent")
#     print("Para execuçãodo Agente do Telegram: python main.py telegram_agent")


setup_logger('whatsapp_agent', 'Logs/whatsapp_agent/{}.log'.format(datetime.now().strftime('%Y-%m-%d')))
logger_whatsapp_agent = logging.getLogger('whatsapp_agent')
logger_whatsapp_agent.info("\nIniciando Agente do WhatsApp.")
cria_assistente(logger_whatsapp_agent)