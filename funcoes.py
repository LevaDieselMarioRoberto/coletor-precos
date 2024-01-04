from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


def inicializa_navegador(maximizado=False):
    """
    Inicializa uma instância do navegador Edge com opções específicas.

    Args:
        maximizado (bool): Indica se a janela do navegador deve ser maximizada (padrão é False).

    Returns:
        WebDriver: Instância do navegador inicializada.
    """

    options = webdriver.EdgeOptions()

    if maximizado:
        # Se maximizado, adiciona argumentos para iniciar maximizado
        options.add_argument("--start-maximized")
        options.add_argument("--force-device-scale-factor=0.8")
    else:
        # Se não maximizado, configura opções para execução sem interface gráfica
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")

    options.add_argument("--enable-chrome-browser-cloud-management")
    options.add_argument("--log-level=1")  # Define o nível de log para WARNING, ERROR e SEVERE

    svc = EdgeService(EdgeChromiumDriverManager().install())    # Configuração do serviço do navegador Edge
    navegador = webdriver.Edge(service=svc, options=options)    # Inicialização do navegador

    return navegador


def clica_botao(navegador, xpath, tempo_espera=20, sleep_time=2):
    """
    Clica em um botão na página da web.

    Args:
        navegador (WebDriver): Instância do navegador Selenium.
        xpath (str): O caminho XPath do botão desejado.
        tempo_espera (int): Tempo máximo de espera para o botão (padrão é 20 segundos).
        sleep_time (int): Tempo de espera adicional após a mudança do modo (padrão é 2 segundos).
    """

    sleep(sleep_time)
    WebDriverWait(navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, xpath))).click()


def preenche_input(navegador, campo, valor, xpath_ou_id='xpath', tempo_espera=20):
    """
    Preenche um campo de entrada na página da web.

    Args:
        navegador (WebDriver): Instância do navegador Selenium.
        campo (str): O ID ou caminho XPath do campo de entrada desejado.
        valor (str): O valor a ser inserido no campo de entrada.
        xpath_ou_id (str): Indica se o campo é identificado por ID ou XPath (padrão é 'xpath').
        tempo_espera (int): Tempo máximo de espera para o campo de entrada (padrão é 20 segundos).
    """

    if xpath_ou_id == 'xpath':
        WebDriverWait(navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, campo))).send_keys(valor)
    elif xpath_ou_id == 'id':
        WebDriverWait(navegador, tempo_espera).until(EC.presence_of_element_located((By.ID, campo))).send_keys(valor)


def seleciona_prazo(navegador, id, prazo, tempo_espera=20):
    """
    Seleciona uma opção de prazo em um menu suspenso na página da web.

    Args:
        navegador (WebDriver): Instância do navegador Selenium.
        id (str): O ID do elemento do menu suspenso.
        prazo (str): O prazo a ser selecionado no menu suspenso.
        tempo_espera (int): Tempo máximo de espera para o menu suspenso (padrão é 20 segundos).
    """

    select_box = WebDriverWait(navegador, tempo_espera).until(EC.presence_of_element_located((By.ID, id)))
    select = Select(select_box)
    select.select_by_visible_text(prazo)


def muda_modo(navegador, id, modo, tempo_espera=20, sleep_time=5):
    """
    Muda o modo em uma página da web.

    Args:
        navegador (WebDriver): Instância do navegador Selenium.
        id (str): O ID do elemento do menu suspenso.
        modo (str): O modo a ser selecionado no menu suspenso.
        tempo_espera (int): Tempo máximo de espera para o menu suspenso (padrão é 20 segundos).
        sleep_time (int): Tempo de espera adicional após a mudança do modo (padrão é 5 segundos).
    """

    select_box = WebDriverWait(navegador, tempo_espera).until(EC.presence_of_element_located((By.ID, id)))
    select = Select(select_box)
    select.select_by_visible_text(modo)
    sleep(sleep_time)


def coleta_valor(navegador, campo, xpath_ou_id='xpath', tempo_espera=20):
    """
    Coleta o valor de um elemento na página da web.

    Args:
        navegador (WebDriver): Instância do navegador Selenium.
        campo (str): O ID ou caminho XPath do elemento desejado.
        xpath_ou_id (str): Indica se o campo é identificado por ID ou XPath (padrão é 'xpath').
        tempo_espera (int): Tempo máximo de espera para o elemento (padrão é 20 segundos).

    Returns:
        float: O valor coletado como um número de ponto flutuante, arredondado para 4 casas decimais.
    """
    if xpath_ou_id == 'xpath':
        return round(
            float(
                WebDriverWait(navegador, tempo_espera)
                .until(EC.presence_of_element_located((By.XPATH, campo)))
                .get_attribute("innerHTML").replace("R$&nbsp;", "").strip().replace(",", ".")
            ), 4
        )
    elif xpath_ou_id == 'id':
        return round(
            float(
                WebDriverWait(navegador, tempo_espera)
                .until(EC.presence_of_element_located((By.ID, campo)))
                .get_attribute("innerHTML").replace("R$&nbsp;", "").strip().replace(",", ".")
            ), 4
        )


def troca_iframe(navegador, xpath_iframe, tempo_espera=5):
    """
    Troca para um iframe específico.

    Args:
        navegador (WebDriver): Instância do navegador Selenium.
        xpath_iframe (str): XPath do elemento iframe.
        tempo_espera (int): Tempo máximo de espera para o elemento (padrão é 5 segundos).
    """

    iframe = WebDriverWait(navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, xpath_iframe)))
    navegador.switch_to.frame(iframe)


def seleciona_opcao_menu_suspenso(navegador, xpath_select_box, opcao, tempo_espera=5):
    """
    Seleciona uma opção em um menu suspenso.

    Args:
        navegador (WebDriver): Instância do navegador Selenium.
        xpath_select_box (str): XPath do elemento do menu suspenso.
        opcao (str): A opção a ser selecionada no menu suspenso.
        tempo_espera (int): Tempo máximo de espera para o elemento (padrão é 5 segundos).
    """
    select_box = WebDriverWait(navegador, tempo_espera).until(EC.presence_of_element_located((By.XPATH, xpath_select_box)))
    select = Select(select_box)
    select.select_by_visible_text(opcao)

    sleep(1)