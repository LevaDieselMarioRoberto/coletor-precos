import requests
import getpass
import os
from dotenv import load_dotenv
from logger import Logger

class Telegram:

    def __init__(self):
        self.env = f"C:/Users/{getpass.getuser()}/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/Informatica/projetos/coleta_precos/.env"
        load_dotenv(self.env)
        self.token = os.getenv('TOKEN')
        self.chat_id = os.getenv('IDCHAT')
    
    def enviar_mensagem(self, msg):
        try:
            data = {"chat_id": self.chat_id, "text": msg}
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            requests.post(url, data)
        except Exception as e:
            logger = Logger()
            logger.log_error("Telegram - Erro no sendMessage:", e)
