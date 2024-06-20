import os

VAR = {
    'tentativas': os.getenv('TENTATIVAS_VBR'),
    'espera_se_erro': int(os.getenv('ESPERA_SE_ERRO_VBR')),

    'link_pedidos': os.getenv('LINK_PEDIDOS_VBR'),
    'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_VBR'),
    'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_VBR'),
    'login': os.getenv('LOGIN_VBR'),
    'senha': os.getenv('SENHA_VBR'),
    'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_VBR'),

    'modal_loading': os.getenv('XPATH_MODAL_LOADING_VBR'),

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
