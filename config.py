import os
from getpass import getuser
from dotenv import load_dotenv

user = getuser()

BASE_DIR = f"C:/Users/{user}/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/Informatica/projetos/coleta_precos/"

PLANILHA_DIR = f"C:/Users/{user}/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/Logística/resultados_precos.xlsx"

ARQUIVO_LOG = BASE_DIR + "dist/coletor.log"
ARQUIVO_ENV = BASE_DIR + ".env" # Necessário ser explícito para execução de tarefa automática do Windows

load_dotenv(ARQUIVO_ENV)

TELEGRAM_CONFIG = {
    'TOKEN': os.getenv('TOKEN'),
    'IDCHAT': os.getenv('IDCHAT'),
}

VAR_IPR_TRR = {
    'link': os.getenv('LINK_IPR'),
    'link_pedidos': os.getenv('LINK_PEDIDOS_IPR'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_IPR'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_IPR'),
    'login': os.getenv('LOGIN_IPR'),
    'senha': os.getenv('SENHA_IPR'),
    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_IPR'),
    'xpath_button_cookies': os.getenv('XPATH_BUTTON_COOKIES_IPR'),
    'xpath_button_pedidos': os.getenv('XPATH_BUTTON_PEDIDOS_IPR'),
    'xpath_select_base': os.getenv('XPATH_SELECT_BASE_IPR'),
    'base': os.getenv('BASE_IPR'),
    'xpath_iframe': os.getenv('XPATH_IFRAME'),
    'xpath_button_razao_social': os.getenv('XPATH_BUTTON_RAZAOSOCIAL_IPRTRR'),
    'xpath_button_ipr2': os.getenv('XPATH_BUTTON_IPR2'),
    'id_preco_cif_s10': os.getenv('ID_PRECO_CIF_S10_IPR_TRR'),
    'id_preco_fob_s10': os.getenv('ID_PRECO_FOB_S10_IPR_TRR'),
    'id_preco_cif_s500': os.getenv('ID_PRECO_CIF_S500_IPR_TRR'),
    'id_preco_fob_s500': os.getenv('ID_PRECO_FOB_S500_IPR_TRR')
}

VAR_IPR_POSTOS = {
    'link': os.getenv('LINK_IPR'),
    'login': os.getenv('LOGIN_IPR_POSTOS'),
    'senha': os.getenv('SENHA_IPR_POSTOS'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_IPR'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_IPR'),
    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_IPR'),
    'xpath_button_cookies': os.getenv('XPATH_BUTTON_COOKIES_IPR'),
    'link_pedidos': os.getenv('LINK_PEDIDOS_IPR'),
    'xpath_button_razaosocial': os.getenv('XPATH_BUTTON_RAZAOSOCIAL_IPRPST'),
    'xpath_iframe': os.getenv('XPATH_IFRAME'),
    'id_preco_cif_etanol': os.getenv('ID_PRECO_CIF_ETANOL_IPR'),
    'id_preco_fob_etanol': os.getenv('ID_PRECO_FOB_ETANOL_IPR'),
    'id_preco_cif_gasolina': os.getenv('ID_PRECO_CIF_GASOLINA_IPR'),
    'id_preco_fob_gasolina': os.getenv('ID_PRECO_FOB_GASOLINA_IPR'),
    'id_preco_cif_gasolinaadt': os.getenv('ID_PRECO_CIF_GASOLINAADT_IPR'),
    'id_preco_fob_gasolinaadt': os.getenv('ID_PRECO_FOB_GASOLINAADT_IPR'),
    'id_preco_cif_s10': os.getenv('ID_PRECO_CIF_S10_IPR'),
    'id_preco_fob_s10': os.getenv('ID_PRECO_FOB_S10_IPR'),
    'id_preco_cif_s500': os.getenv('ID_PRECO_CIF_S500_IPR'),
    'id_preco_fob_s500': os.getenv('ID_PRECO_FOB_S500_IPR'),
    'xpath_button_distrito': os.getenv('XPATH_BUTTON_DISTRITO_IPR'),
    'xpath_button_itirapua': os.getenv('XPATH_BUTTON_ITIRAPUA_IPR'),
    'xpath_button_ppp': os.getenv('XPATH_BUTTON_PPP_IPR'),
    'xpath_button_pitstop': os.getenv('XPATH_BUTTON_PITSTOP_IPR')
}

VAR_VBR_TRR = {
    'link': os.getenv('LINK_VBR'),
    'login': os.getenv('LOGIN_VBR'),
    'senha': os.getenv('SENHA_VBR'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_VBR'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_VBR'),
    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_VBR'),
    'link_pedidos': os.getenv('LINK_PEDIDOS_VBR'),
    'id_input_qtdlitros_s10': os.getenv('ID_INPUT_QTDLITROS_S10_VBR'),
    'id_input_qtdlitros_s500': os.getenv('ID_INPUT_QTDLITROS_S500_VBR'),
    'xpath_button_atualizar': os.getenv('XPATH_BUTTON_ATUALIZAR_VBR'),
    'id_select_prazo_s10': os.getenv('ID_SELECT_PRAZO_S10_VBR'),
    'id_select_prazos500': os.getenv('ID_SELECT_PRAZO_S500_VBR'),
    'prazo': os.getenv('PRAZO_VBR'),
    'xpath_preco_s10': os.getenv('XPATH_PRECO_S10_VBR'),
    'xpath_preco_s500': os.getenv('XPATH_PRECO_S500_VBR'),
    'id_select_modo_s10': os.getenv('ID_SELECT_MODO_S10_VBR'),
    'id_select_modo_s500': os.getenv('ID_SELECT_MODO_S500_VBR'),
    'modo': os.getenv('MODO_VBR')
}

VAR_VBR_JJ = {
    'link': os.getenv('LINK_VBR'),
    'login': os.getenv('LOGIN_VBR_JANJAO'),
    'senha': os.getenv('SENHA_VBR_JANJAO'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_VBR'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_VBR'),
    'link_pedidos': os.getenv('LINK_PEDIDOS_VBR'),
    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_VBR'),
    'xpath_button_atualizar': os.getenv('XPATH_BUTTON_ATUALIZAR_VBR'),
    'xpath_preco_etanol': os.getenv('XPATH_PRECO_ETANOL_VBRJJ'),
    'xpath_preco_gasolina': os.getenv('XPATH_PRECO_GASOLINA_VBRJJ'),
    'xpath_preco_s10': os.getenv('XPATH_PRECO_S10_VBRJJ'),
    'xpath_preco_s500': os.getenv('XPATH_PRECO_S500_VBRJJ'),
    'modo': os.getenv('MODO_VBR'),
    'id_select_modo_etanol': os.getenv('ID_SELECT_MODO_ETANOL_VBRJJ'),
    'id_select_modo_gasolina': os.getenv('ID_SELECT_MODO_GASOLINA_VBRJJ'),
    'id_select_modo_s10': os.getenv('ID_SELECT_MODO_S10_VBRJJ'),
    'id_select_modo_s500': os.getenv('ID_SELECT_MODO_S500_VBRJJ')
}

VAR_RZN_TRR = {
    'link': os.getenv('LINK_RZN'),
    'login': os.getenv('LOGIN_RZN'),
    'senha': os.getenv('SENHA_RZN'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_RZN'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_RZN'),
    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_RZN'),
    'link_precos': os.getenv('LINK_PRECOS_RZN'),
    'xpath_preco_fob_s10': os.getenv('XPATH_PRECO_FOB_S10_RZN'),
    'xpath_preco_fob_s500': os.getenv('XPATH_PRECO_FOB_S500_RZN'),
    'xpath_preco_cif_s10': os.getenv('XPATH_PRECO_CIF_S10_RZN'),
    'xpath_preco_cif_s500': os.getenv('XPATH_PRECO_CIF_S500_RZN')
}
