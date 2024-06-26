from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from config.config import BASE_DIR
import json


class ColetorDePreco(ABC):

    def __init__(self):
        self.inicio = None
        self.tempo_execucao = None
        self.navegador = None

    def inicializa_navegador(self, maximizado, browser='edge'):
        """
        Inicializa uma instância do navegador Edge com opções específicas.
        """
        if browser == 'edge': options = webdriver.EdgeOptions()
        elif browser == 'firefox': options = webdriver.FirefoxOptions()

        if maximizado:
            options.add_argument("--start-maximized")
            options.add_argument("--force-device-scale-factor=0.8")
        else:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            if browser == 'edge': options.add_argument("--window-size=1920x1080")

        options.add_argument("--log-level=1")

        if browser == 'edge':
            options.add_argument("--enable-chrome-browser-cloud-management")
            svc = EdgeService(EdgeChromiumDriverManager().install())
            navegador = webdriver.Edge(service=svc, options=options)
        elif browser == 'firefox':
            svc = FirefoxService(executable_path=GeckoDriverManager().install())
            navegador = webdriver.Firefox(service=svc, options=options)

        return navegador

    def clica_botao(self, xpath, tempo_espera=20, sleep_time=2):
        """
        Clica em um botão na página da web.
        """
        sleep(sleep_time)
        WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, xpath))).click()

    def preenche_input(self, campo, valor, xpath_ou_id='xpath', tempo_espera=20):
        """
        Preenche um campo de input na página da web.
        """
        if xpath_ou_id == 'xpath':
            WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, campo))).send_keys(valor)
        elif xpath_ou_id == 'id':
            WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.ID, campo))).send_keys(valor)

    def seleciona_prazo(self, id, prazo, tempo_espera=20):
        """ 
        Seleciona uma opção de prazo em um menu suspenso na página da web.
        """
        select_box = WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.ID, id)))
        select = Select(select_box)
        select.select_by_visible_text(prazo)

    def muda_modo(self, id, modo, tempo_espera=20, sleep_time=5):
        """
        Muda o modo em uma página da web.
        """
        select_box = WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.ID, id)))
        select = Select(select_box)
        select.select_by_visible_text(modo)
        sleep(sleep_time)

    def coleta_valor(self, campo, xpath_ou_id='xpath', tempo_espera=20):
        """
        Coleta o valor de um elemento na página da web.
        """
        if xpath_ou_id == 'xpath':
            return round(
                float(
                    WebDriverWait(self.navegador, tempo_espera)
                    .until(EC.presence_of_element_located((By.XPATH, campo)))
                    .get_attribute("innerHTML").replace("R$&nbsp;", "").strip().replace(",", ".")
                ), 4
            )
        elif xpath_ou_id == 'id':
            return round(
                float(
                    WebDriverWait(self.navegador, tempo_espera)
                    .until(EC.presence_of_element_located((By.ID, campo)))
                    .get_attribute("innerHTML").replace("R$&nbsp;", "").strip().replace(",", ".")
                ), 4
            )

    def troca_iframe(self, xpath_iframe, tempo_espera=5):
        """
        Troca para um iframe específico.
        """
        iframe = WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, xpath_iframe)))
        self.navegador.switch_to.frame(iframe)

    def seleciona_opcao_menu_suspenso(self, xpath_select_box, opcao, tempo_espera=5):
        """
        Seleciona uma opção em um menu suspenso.
        """
        select_box = WebDriverWait(self.navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, xpath_select_box)))
        select = Select(select_box)
        select.select_by_visible_text(opcao)
        sleep(1)

    def fechar_navegador(self):
        """ 
        Fecha o navegador. 
        """
        self.navegador.quit()

    def __consulta_json_erro(self, filename):
        """
        Consulta o arquivo JSON de erro.
        """
        arquivo_json = BASE_DIR + f"dist/{filename}-erro.json"
        try:
            with open(arquivo_json, 'r') as f: erro_anterior = json.load(f)
            return erro_anterior
        except: return {}
    
    def __salva_json_erro(self, filename, content):
        """
        Salva o conteúdo de um arquivo JSON.
        """
        arquivo_json = BASE_DIR + f"dist/{filename}-erro.json"
        with open(arquivo_json, 'w') as f: json.dump(content, f, indent=2)

    def estava_com_erro(self, filename):
        """
        Verifica se a última coleta de preços estava com erro.
        """
        erro_anterior = self.__consulta_json_erro(filename)

        if erro_anterior == {}: return False

        self.__salva_json_erro(filename, {})
        contagem_erros = erro_anterior["contagem_erros"]
        if contagem_erros > 2: return True
        return False

    def eh_terceiro_erro_consecutivo(self, filename, error):
        """
        Verifica se houve terceiro erro consecutivo.
        """
        erro_anterior = self.__consulta_json_erro(filename)

        try: contagem_erros = erro_anterior["contagem_erros"]
        except: contagem_erros = 0

        if contagem_erros != 2:
            self.__salva_json_erro(filename, {"erro": str(error), "contagem_erros": contagem_erros + 1})
            return False
        elif contagem_erros == 2:
            self.__salva_json_erro(filename, {"erro": str(error), "contagem_erros": contagem_erros + 1})
            return True

    @abstractmethod
    def coleta_precos(self, maximizado=False):
        pass
