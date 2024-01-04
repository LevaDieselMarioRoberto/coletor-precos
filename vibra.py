from config import var_vbr as VAR
from funcoes import inicializa_navegador, clica_botao, preenche_input, seleciona_prazo, muda_modo, coleta_valor
from time import time

def coleta_precos(maximizado=False):
    """
    Coleta preços de produtos em uma página da web usando Selenium.

    Args:
        maximizado (bool): Indica se a janela do navegador deve ser maximizada (padrão é False).

    Returns:
        tuple: Um tupla contendo um dicionário de preços e o tempo de execução.
    """

    inicio = time()
    navegador = inicializa_navegador(maximizado)

    with navegador:

        # Login na página principal
        navegador.get(VAR['link'])
        preenche_input(navegador, VAR['xpath_input_login'], VAR['login'])
        preenche_input(navegador, VAR['xpath_input_senha'], VAR['senha'])
        clica_botao(navegador, VAR['xpath_button_entrar'])

        # Navegação para a página de pedidos e preenchimento dos campos de quantidade
        navegador.get(VAR['link_pedidos'])
        preenche_input(navegador, VAR['id_input_qtdlitros_s10'], 10000, xpath_ou_id='id')
        preenche_input(navegador, VAR['id_input_qtdlitros_s500'], 10000, xpath_ou_id='id')
        clica_botao(navegador, VAR['xpath_button_atualizar'], sleep_time=5)

        # Seleção de prazo
        seleciona_prazo(navegador, VAR['id_select_prazo_s10'], VAR['prazo'])
        seleciona_prazo(navegador, VAR['id_select_prazos500'], VAR['prazo'])
        clica_botao(navegador, VAR['xpath_button_atualizar'], sleep_time=8)

        precos_vbr = {}

        # Coleta de preços FOB
        precos_vbr['fob_s10'] = coleta_valor(navegador, VAR['xpath_preco_s10'])
        precos_vbr['fob_s500'] = coleta_valor(navegador, VAR['xpath_preco_s500'])

        # Alteração de modo
        muda_modo(navegador, VAR['id_select_modo_s10'], VAR['modo'])
        muda_modo(navegador, VAR['id_select_modo_s500'], VAR['modo'])
        clica_botao(navegador, VAR['xpath_button_atualizar'], sleep_time=5)

        # Coleta de preços CIF
        precos_vbr['cif_s10'] = coleta_valor(navegador, VAR['xpath_preco_s10'])
        precos_vbr['cif_s500'] = coleta_valor(navegador, VAR['xpath_preco_s500'])

    tempo_execucao = round(time() - inicio, 2)

    return precos_vbr, tempo_execucao


if __name__ == "__main__":

    precos_vbr, tempo_execucao = coleta_precos(maximizado=True)

    print("\n----------------------------------")
    print(f"                CIF           FOB       ({tempo_execucao}s)")
    print("Preços Vibra TRR:")
    print(f"s10            {precos_vbr['cif_s10']}       {precos_vbr['fob_s10']}")
    print(f"s500           {precos_vbr['cif_s500']}       {precos_vbr['fob_s500']}")
    print("----------------------------------")
