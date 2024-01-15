import logging

class Logger:

    def __init__(self):
        self.arquivo_log = "C:/Users/titrr/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/Informatica/projetos/coleta_precos/dist/coletor.log"
        self.log_format = '%(asctime)s - %(levelname)s - %(message)s'
        logging.basicConfig(filename=self.arquivo_log, level=logging.INFO, format=self.log_format, encoding='utf-8')

    def log(self, msg):
        logging.info(msg)
    
    def log_error(self, msg):
        logging.error(msg)
