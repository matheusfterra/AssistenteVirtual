import DBConnectors.DBUsers, DBConnectors.Constants
import Functions.AccountAgent
from time import sleep

class AssistentEngine:

    def __init__(self, webdriver = None):
        self.webdriver = webdriver
        print("Executando Software\n")

    def whatsapp_agent(self,logger):
        Functions.AccountAgent.acesso_whatsapp(logger,self.webdriver)





