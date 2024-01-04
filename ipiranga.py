from config import var_ipr as VAR
from funcoes import inicializa_navegador, clica_botao, preenche_input, coleta_valor, troca_iframe, seleciona_opcao_menu_suspenso
from time import time

def coleta_precos(maximizado=False):
    """
    Coleta preços de produtos em uma página da web usando Selenium.

    Args:
        maximizado (bool): Indica se a janela do navegador deve ser maximizada (padrão é False).

    Returns:
        tuple: Um tupla contendo dois dicionários de preços e o tempo de execução.
    """

    inicio = time()
    navegador = inicializa_navegador(maximizado)

    with navegador:

        # Login na página principal
        navegador.get(VAR['link'])
        preenche_input(navegador, VAR['xpath_input_login'], VAR['login'])
        preenche_input(navegador, VAR['xpath_input_senha'], VAR['senha'])
        clica_botao(navegador, VAR['xpath_button_entrar'])
        clica_botao(navegador, VAR['xpath_button_cookies'])
        clica_botao(navegador, VAR['xpath_button_pedidos'])

        # Troca para o iframe e seleciona a base
        troca_iframe(navegador, VAR['xpath_iframe'])
        seleciona_opcao_menu_suspenso(navegador, VAR['xpath_select_base'], VAR['base'])

        precos_ipr1 = {}    # Coleta os preços do primeiro perfil da TRR
        precos_ipr1['cif_s10'] = coleta_valor(navegador, VAR['id_preco_cif_s10'], xpath_ou_id='id')
        precos_ipr1['fob_s10'] = coleta_valor(navegador, VAR['id_preco_fob_s10'], xpath_ou_id='id')
        precos_ipr1['cif_s500'] = coleta_valor(navegador, VAR['id_preco_cif_s500'], xpath_ou_id='id')
        precos_ipr1['fob_s500'] = coleta_valor(navegador, VAR['id_preco_fob_s500'], xpath_ou_id='id')

        # Troca para o segundo perfil da TRR
        navegador.get(VAR['link_pedidos'])
        clica_botao(navegador, VAR['xpath_button_razao_social'])
        clica_botao(navegador, VAR['xpath_button_ipr2'])
        
        # Troca para o iframe e seleciona a base
        troca_iframe(navegador, VAR['xpath_iframe'])
        seleciona_opcao_menu_suspenso(navegador, VAR['xpath_select_base'], VAR['base'])

        precos_ipr2 = {}    # Coleta os preços do segundo perfil da TRR
        precos_ipr2['cif_s10'] = coleta_valor(navegador, VAR['id_preco_cif_s10'], xpath_ou_id='id')
        precos_ipr2['fob_s10'] = coleta_valor(navegador, VAR['id_preco_fob_s10'], xpath_ou_id='id')
        precos_ipr2['cif_s500'] = coleta_valor(navegador, VAR['id_preco_cif_s500'], xpath_ou_id='id')
        precos_ipr2['fob_s500'] = coleta_valor(navegador, VAR['id_preco_fob_s500'], xpath_ou_id='id')

    tempo_execucao = round(time() - inicio, 2)

    return precos_ipr1, precos_ipr2, tempo_execucao


if __name__ == "__main__":

    precos_ipr1, precos_ipr2, tempo_execucao = coleta_precos(maximizado=True)

    print("\n----------------------------------")
    print(f"                CIF           FOB       ({tempo_execucao}s)")
    print(f"Preços Ipiranga TRR [1]:")
    print(f"s10            {round(precos_ipr1['cif_s10'], 4)}       {round(precos_ipr1['fob_s10'], 4)}")
    print(f"s500           {round(precos_ipr1['cif_s500'], 4)}       {round(precos_ipr1['fob_s500'], 4)}")
    print(f"Preços Ipiranga TRR [2]:")
    print(f"s10            {round(precos_ipr2['cif_s10'], 4)}       {round(precos_ipr2['fob_s10'], 4)}")
    print(f"s500           {round(precos_ipr2['cif_s500'], 4)}       {round(precos_ipr2['fob_s500'], 4)}")
    print("----------------------------------")
