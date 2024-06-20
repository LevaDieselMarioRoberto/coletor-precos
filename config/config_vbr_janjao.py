import os

VAR = {
    'tentativas': os.getenv('TENTATIVAS_VBR'),
    'espera_se_erro': int(os.getenv('ESPERA_SE_ERRO_VBR')),

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
