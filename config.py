import os
from getpass import getuser
from dotenv import load_dotenv

user = getuser()

BASE_DIR = f"C:/Users/{user}/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/Informatica/projetos/coletor_precos/"

PLANILHA_DIR = f"C:/Users/{user}/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/Logística/resultados_precos.xlsx"

ARQUIVO_LOG = BASE_DIR + "dist/coletor.log"
ARQUIVO_ENV = BASE_DIR + ".env" # Necessário ser explícito para execução de tarefa automática do Windows

load_dotenv(ARQUIVO_ENV)

CONTROLS = {
    'COLETA_HABILITADA': os.getenv('COLETA_HABILITADA', 'true').lower() == 'true',
    'COLETAR_IPR_TRR': os.getenv('COLETAR_IPR_TRR', 'true').lower() == 'true',
    'COLETAR_VBR_TRR': os.getenv('COLETAR_VBR_TRR', 'true').lower() == 'true',
    'COLETAR_RZN_TRR': os.getenv('COLETAR_RZN_TRR', 'true').lower() == 'true',
    'COLETAR_VBR_JJ': os.getenv('COLETAR_VBR_JJ', 'true').lower() == 'true',
    'COLETAR_IPR_POSTOS': os.getenv('COLETAR_IPR_POSTOS', 'true').lower() == 'true',
    'MAXIMIZADO_IPR_TRR': os.getenv('MAXIMIZADO_IPR_TRR', 'false').lower() == 'true',
    'MAXIMIZADO_VBR_TRR': os.getenv('MAXIMIZADO_VBR_TRR', 'false').lower() == 'true',
    'MAXIMIZADO_RZN_TRR': os.getenv('MAXIMIZADO_RZN_TRR', 'false').lower() == 'true',
    'MAXIMIZADO_VBR_JJ': os.getenv('MAXIMIZADO_VBR_JJ', 'false').lower() == 'true',
    'MAXIMIZADO_IPR_POSTOS': os.getenv('MAXIMIZADO_IPR_POSTOS', 'false').lower() == 'true',
    'IMPRIME_PRECOS_TERMINAL': os.getenv('IMPRIME_PRECOS_TERMINAL', 'false').lower() == 'true',
    'SALVA_PRECOS_PLANILHA': os.getenv('SALVA_PRECOS_PLANILHA', 'false').lower() == 'true',
    'ENVIA_PRECOS_TELEGRAM': os.getenv('ENVIA_PRECOS_TELEGRAM', 'false').lower() == 'true',
}

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
    'link_pedidos': os.getenv('LINK_PEDIDOS_VBR'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_VBR'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_VBR'),
    'login': os.getenv('LOGIN_VBR'),
    'senha': os.getenv('SENHA_VBR'),
    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_VBR'),

    'xpath_checkbox_revenda': os.getenv('XPATH_CHECKBOX_REVENDA_VBR'),
    'id_input_qtdlitros_s10': os.getenv('ID_INPUT_QTDLITROS_S10_VBR'),
    'id_input_qtdlitros_s500': os.getenv('ID_INPUT_QTDLITROS_S500_VBR'),
    'xpath_button_atualizar': os.getenv('XPATH_BUTTON_ATUALIZAR_VBR'),

    'id_select_prazo_s10': os.getenv('ID_SELECT_PRAZO_S10_VBR'),
    'id_select_prazos500': os.getenv('ID_SELECT_PRAZO_S500_VBR'),
    'prazo': os.getenv('PRAZO_VBR'),

    'id_select_modo': os.getenv('ID_SELECT_MODO_VBRJJ'),
    'modo': os.getenv('MODO_VBR'),

    'xpath_preco_s10': os.getenv('XPATH_PRECO_S10_VBR'),
    'xpath_preco_s500': os.getenv('XPATH_PRECO_S500_VBR'),
}

VAR_VBR_JJ = {
    'link_pedidos': os.getenv('LINK_PEDIDOS_VBR'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_VBR'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_VBR'),
    'login': os.getenv('LOGIN_VBR_JANJAO'),
    'senha': os.getenv('SENHA_VBR_JANJAO'),
    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_VBR'),

    'xpath_preco_etanol': os.getenv('XPATH_PRECO_ETANOL_VBRJJ'),
    'xpath_preco_gasolina': os.getenv('XPATH_PRECO_GASOLINA_VBRJJ'),
    'xpath_preco_s10': os.getenv('XPATH_PRECO_S10_VBRJJ'),
    'xpath_preco_s500': os.getenv('XPATH_PRECO_S500_VBRJJ'),

    'modo': os.getenv('MODO_VBR'),
    'id_select_modo': os.getenv('ID_SELECT_MODO_VBRJJ'),
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
