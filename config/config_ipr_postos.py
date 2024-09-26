import os
from getpass import getuser
from dotenv import load_dotenv

user = getuser()
BASE_DIR = f"C:/Users/{user}/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/Informatica/projetos/coletor_precos/"
ARQUIVO_ENV = f"{BASE_DIR}.env" # Necessário ser explícito para execução de tarefa automática do Windows

load_dotenv(ARQUIVO_ENV)

VAR = {
    'tentativas': os.getenv('TENTATIVAS_IPR'),
    'espera_se_erro': os.getenv('ESPERA_SE_ERRO_IPR'),

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
    'xpath_button_acesso': os.getenv('XPATH_BUTTON_ACESSO_IPR'),
    'xpath_button_ppp': os.getenv('XPATH_BUTTON_PPP_IPR'),
    'xpath_button_pitstop': os.getenv('XPATH_BUTTON_PITSTOP_IPR')
}
