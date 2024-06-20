import os

VAR = {
    'tentativas': os.getenv('TENTATIVAS_RZN'),
    'espera_se_erro': int(os.getenv('ESPERA_SE_ERRO_RZN')),
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