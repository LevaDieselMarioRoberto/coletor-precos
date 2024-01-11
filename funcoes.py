from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep, time


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
        sleep_time (int): Tempo de espera adicional antes do clique (padrão é 2 segundos).
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


def imprime_precos(
    precos_ipr1, precos_ipr2, tempo_ex_ipr,
    precos_vbr, tempo_ex_vbr,
    precos_rzn, tempo_ex_rzn,
    precos_gasstation, precos_distrito, precos_itirapua, precos_ppp, precos_pitstop, tempo_ex_ipr_postos,
    precos_vbr_janjao, tempo_ex_vbr_janjao,
    inicio
):
    """
    Imprime os preços coletados.

    Args:
        precos_ipr1 (dict): Dicionário com os preços coletados do posto Ipiranga 1.
        precos_ipr2 (dict): Dicionário com os preços coletados do posto Ipiranga 2.
        tempo_ex_ipr (float): Tempo de execução da coleta de preços do posto Ipiranga.
        precos_vbr (dict): Dicionário com os preços coletados do posto Vibra.
        tempo_ex_vbr (float): Tempo de execução da coleta de preços do posto Vibra.
        precos_rzn (dict): Dicionário com os preços coletados do posto Raizen.
        tempo_ex_rzn (float): Tempo de execução da coleta de preços do posto Raizen.
        precos_gasstation (dict): Dicionário com os preços coletados do posto Ipiranga Gas Station.
        precos_distrito (dict): Dicionário com os preços coletados do posto Ipiranga Distrito.
        precos_itirapua (dict): Dicionário com os preços coletados do posto Ipiranga Itirapuã.
        precos_ppp (dict): Dicionário com os preços coletados do posto Ipiranga PPP.
        precos_pitstop (dict): Dicionário com os preços coletados do posto Ipiranga Pit Stop.
        tempo_ex_ipr_postos (float): Tempo de execução da coleta de preços dos postos Ipiranga.
        precos_vbr_janjao (dict): Dicionário com os preços coletados do posto Vibra Janjão.
        tempo_ex_vbr_janjao (float): Tempo de execução da coleta de preços do posto Vibra Janjão.
        inicio (float): Tempo de início da execução do script.
    """
    print("\n----------------------------------")
    print("                CIF           FOB\n")

    print("TRR:\n")

    print(f"Ipiranga [1]:              ({tempo_ex_ipr}s)")
    print(f"s10            {precos_ipr1['cif_s10']}       {precos_ipr1['fob_s10']}")
    print(f"s500           {precos_ipr1['cif_s500']}       {precos_ipr1['fob_s500']}")
    print(f"Ipiranga [2]:")
    print(f"s10            {precos_ipr2['cif_s10']}       {precos_ipr2['fob_s10']}")
    print(f"s500           {precos_ipr2['cif_s500']}       {precos_ipr2['fob_s500']}\n")

    print(f"Vibra:                     ({tempo_ex_vbr}s)")
    print(f"s10            {precos_vbr['cif_s10']}       {precos_vbr['fob_s10']}")
    print(f"s500           {precos_vbr['cif_s500']}       {precos_vbr['fob_s500']}\n")

    print(f"Raizen:                    ({tempo_ex_rzn}s)")
    print(f"s10            {precos_rzn['cif_s10']}       {precos_rzn['fob_s10']}")
    print(f"s500           {precos_rzn['cif_s500']}       {precos_rzn['fob_s500']}\n")

    print("\nPostos:\n")

    print(f"Ipiranga Gás Station:      ({tempo_ex_ipr_postos}s)")
    print(f"Etanol         {precos_gasstation['cif_etanol']}       {precos_gasstation['fob_etanol']}")
    print(f"Gasolina       {precos_gasstation['cif_gasolina']}       {precos_gasstation['fob_gasolina']}")
    print(f"Gasolina Ad    {precos_gasstation['cif_gasolina_adt']}       {precos_gasstation['fob_gasolina_adt']}")
    print(f"s10            {precos_gasstation['cif_s10']}       {precos_gasstation['fob_s10']}\n")

    print("Ipiranga Distrito:")
    print(f"Etanol         {precos_distrito['cif_etanol']}       {precos_distrito['fob_etanol']}")
    print(f"Gasolina       {precos_distrito['cif_gasolina']}       {precos_distrito['fob_gasolina']}")
    print(f"s10            {precos_distrito['cif_s10']}       {precos_distrito['fob_s10']}")
    print(f"s500           {precos_distrito['cif_s500']}       {precos_distrito['fob_s500']}\n")

    print("Ipiranga Itirapuã:")
    print(f"Etanol         {precos_itirapua['cif_etanol']}       {precos_itirapua['fob_etanol']}")
    print(f"Gasolina       {precos_itirapua['cif_gasolina']}       {precos_itirapua['fob_gasolina']}")
    print(f"s10            {precos_itirapua['cif_s10']}       {precos_itirapua['fob_s10']}")
    print(f"s500           {precos_itirapua['cif_s500']}       {precos_itirapua['fob_s500']}\n")

    print("Ipiranga PPP:")
    print(f"Etanol         {precos_ppp['cif_etanol']}       {precos_ppp['fob_etanol']}")
    print(f"Gasolina       {precos_ppp['cif_gasolina']}       {precos_ppp['fob_gasolina']}")
    print(f"s10            {precos_ppp['cif_s10']}       {precos_ppp['fob_s10']}\n")

    print("Ipiranga Pit Stop:")
    print(f"Etanol         {precos_pitstop['cif_etanol']}       {precos_pitstop['fob_etanol']}")
    print(f"Gasolina       {precos_pitstop['cif_gasolina']}       {precos_pitstop['fob_gasolina']}")
    print(f"Gasolina Ad    {precos_pitstop['cif_gasolina_adt']}       {precos_pitstop['fob_gasolina_adt']}")
    print(f"s10            {precos_pitstop['cif_s10']}       {precos_pitstop['fob_s10']}")
    print(f"s500           {precos_pitstop['cif_s500']}       {precos_pitstop['fob_s500']}\n")

    print(f"Vibra Janjão:              ({tempo_ex_vbr_janjao}s)")
    print(f"Etanol         {precos_vbr_janjao['cif_etanol']}       {precos_vbr_janjao['fob_etanol']}")
    print(f"Gasolina       {precos_vbr_janjao['cif_gasolina']}       {precos_vbr_janjao['fob_gasolina']}")
    print(f"s10            {precos_vbr_janjao['cif_s10']}       {precos_vbr_janjao['fob_s10']}")
    print(f"s500           {precos_vbr_janjao['cif_s500']}       {precos_vbr_janjao['fob_s500']}\n")

    print(f"Tempo total: {round(time() - inicio, 2)} segundos")
    print("----------------------------------")


def cria_dicionario_para_df(
    precos_ipr1, precos_ipr2, precos_vbr, precos_rzn,
    precos_gasstation, precos_distrito, precos_itirapua, precos_ppp, precos_pitstop, tempo_ex_ipr_postos,
    precos_vbr_janjao,    
):
    """
    Cria um dicionário com os preços coletados para ser usado na criação de um DataFrame.

    Args:
        precos_ipr1 (dict): Dicionário com os preços coletados do posto Ipiranga 1.
        precos_ipr2 (dict): Dicionário com os preços coletados do posto Ipiranga 2.
        precos_vbr (dict): Dicionário com os preços coletados do posto Vibra.
        precos_rzn (dict): Dicionário com os preços coletados do posto Raizen.
        precos_gasstation (dict): Dicionário com os preços coletados do posto Ipiranga Gas Station.
        precos_distrito (dict): Dicionário com os preços coletados do posto Ipiranga Distrito.
        precos_itirapua (dict): Dicionário com os preços coletados do posto Ipiranga Itirapuã.
        precos_ppp (dict): Dicionário com os preços coletados do posto Ipiranga PPP.
        precos_pitstop (dict): Dicionário com os preços coletados do posto Ipiranga Pit Stop.
        tempo_ex_ipr_postos (float): Tempo de execução da coleta de preços dos postos Ipiranga.
        precos_vbr_janjao (dict): Dicionário com os preços coletados do posto Vibra Janjão.
    """
    return {
        "TIPO": ["Etanol", "Gas Ad", "Gas C", "S10", "S500"],
        "CIF2": [precos_pitstop['cif_etanol'], precos_pitstop['cif_gasolina_adt'], precos_pitstop['cif_gasolina'], precos_pitstop['cif_s10'], precos_pitstop['cif_s500']],
        "FOB2": [precos_pitstop['fob_etanol'], precos_pitstop['fob_gasolina_adt'], precos_pitstop['fob_gasolina'], precos_pitstop['fob_s10'], precos_pitstop['fob_s500']],
        "CIF3": [precos_distrito['cif_etanol'], '', precos_distrito['cif_gasolina'], precos_distrito['cif_s10'], precos_distrito['cif_s500']],
        "FOB3": [precos_distrito['fob_etanol'], '', precos_distrito['fob_gasolina'], precos_distrito['fob_s10'], precos_distrito['fob_s500']],
        "CIF4": [precos_gasstation['cif_etanol'], precos_gasstation['cif_gasolina_adt'], precos_gasstation['cif_gasolina'], precos_gasstation['cif_s10'], ''],
        "FOB4": [precos_gasstation['fob_etanol'], precos_gasstation['fob_gasolina_adt'], precos_gasstation['fob_gasolina'], precos_gasstation['fob_s10'], ''],
        "CIF5": [precos_itirapua['cif_etanol'], '', precos_itirapua['cif_gasolina'], precos_itirapua['cif_s10'], precos_itirapua['cif_s500']],
        "FOB5": [precos_itirapua['fob_etanol'], '', precos_itirapua['fob_gasolina'], precos_itirapua['fob_s10'], precos_itirapua['fob_s500']],
        "CIF6": [precos_ppp['cif_etanol'], '', precos_ppp['cif_gasolina'], precos_ppp['cif_s10'], ''],
        "FOB6": [precos_ppp['fob_etanol'], '', precos_ppp['fob_gasolina'], precos_ppp['fob_s10'], ''],
        "CIF7": [precos_vbr_janjao['cif_etanol'], '', precos_vbr_janjao['cif_gasolina'], precos_vbr_janjao['cif_s10'], precos_vbr_janjao['cif_s500']],
        "FOB7": [precos_vbr_janjao['fob_etanol'], '', precos_vbr_janjao['fob_gasolina'], precos_vbr_janjao['fob_s10'], precos_vbr_janjao['fob_s500']],
        "CIF8": ['', '', '', precos_ipr1['cif_s10'], precos_ipr1['cif_s500']],
        "FOB8": ['', '', '', precos_ipr1['fob_s10'], precos_ipr1['fob_s500']],
        "CIF9": ['', '', '', precos_ipr2['cif_s10'], precos_ipr2['cif_s500']],
        "FOB9": ['', '', '', precos_ipr2['fob_s10'], precos_ipr2['fob_s500']],
        "CIF10": ['', '', '', precos_vbr['cif_s10'], precos_vbr['cif_s500']],
        "FOB10": ['', '', '', precos_vbr['fob_s10'], precos_vbr['fob_s500']],
        "CIF11": ['', '', '', precos_rzn['cif_s10'], precos_rzn['cif_s500']],
        "FOB11": ['', '', '', precos_rzn['fob_s10'], precos_rzn['fob_s500']]
    }
