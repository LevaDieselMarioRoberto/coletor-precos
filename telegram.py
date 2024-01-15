import requests
from logger import Logger

class Telegram:

    token = '6549384225:AAEBaKjBcOcY8jL_g6A81L9wIprhQuSZJNY'
    chat_id = -1002070343424
    
    def enviar_mensagem(self, msg):
        try:
            data = {"chat_id": self.chat_id, "text": msg}
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            requests.post(url, data)
        except Exception as e:
            logger = Logger()
            logger.log_error("Telegram - Erro no sendMessage:", e)
