import os
from getpass import getuser
from dotenv import load_dotenv

user = getuser()
BASE_DIR = f"C:/Users/{user}/Documents/Projetos/coletor_precos/"
ARQUIVO_ENV = f"{BASE_DIR}.env" # Necessário ser explícito para execução de tarefa automática do Windows

load_dotenv(ARQUIVO_ENV)

VAR = {
    'tentativas': os.getenv('TENTATIVAS_IPR'),
    'espera_se_erro': os.getenv('ESPERA_SE_ERRO_IPR'),

    'link_pedidos': os.getenv('LINK_PEDIDOS_IPR'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_IPR'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_IPR'),
    'login': os.getenv('LOGIN_IPR'),
    'senha': os.getenv('SENHA_IPR'),

    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_IPR'),
    'xpath_button_cookies': os.getenv('XPATH_BUTTON_COOKIES_IPR'),

    'xpath_button_razao_social': os.getenv('XPATH_BUTTON_RAZAOSOCIAL_IPRTRR'),
    'xpath_button_ipr2': os.getenv('XPATH_BUTTON_IPR2'),

    'xpath_iframe': os.getenv('XPATH_IFRAME'),
    'xpath_select_base': os.getenv('XPATH_SELECT_BASE_IPR'),
    'base': os.getenv('BASE_IPR'),

    'id_preco_cif_s10': os.getenv('ID_PRECO_CIF_S10_IPR_TRR'),
    'id_preco_fob_s10': os.getenv('ID_PRECO_FOB_S10_IPR_TRR'),
    'id_preco_cif_s500': os.getenv('ID_PRECO_CIF_S500_IPR_TRR'),
    'id_preco_fob_s500': os.getenv('ID_PRECO_FOB_S500_IPR_TRR')
}
