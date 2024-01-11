from config import var_vbr_janjao as VAR
from funcoes import inicializa_navegador, clica_botao, preenche_input, muda_modo, coleta_valor
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

        # Navegação para a página de pedidos
        navegador.get(VAR['link_pedidos'])

        precos_vbr = {}

        # Coleta de preços FOB
        precos_vbr['fob_etanol'] = coleta_valor(navegador, VAR['xpath_preco_etanol'])
        precos_vbr['fob_gasolina'] = coleta_valor(navegador, VAR['xpath_preco_gasolina'])
        precos_vbr['fob_s10'] = coleta_valor(navegador, VAR['xpath_preco_s10'])
        precos_vbr['fob_s500'] = coleta_valor(navegador, VAR['xpath_preco_s500'])

        # Alteração de modo
        muda_modo(navegador, VAR['id_select_modo_etanol'], VAR['modo'])
        muda_modo(navegador, VAR['id_select_modo_gasolina'], VAR['modo'])
        muda_modo(navegador, VAR['id_select_modo_s10'], VAR['modo'])
        muda_modo(navegador, VAR['id_select_modo_s500'], VAR['modo'])
        clica_botao(navegador, VAR['xpath_button_atualizar'], sleep_time=5)
        clica_botao(navegador, VAR['xpath_button_atualizar'], sleep_time=5)

        # Coleta de preços CIF
        precos_vbr['cif_etanol'] = coleta_valor(navegador, VAR['xpath_preco_etanol'])
        precos_vbr['cif_gasolina'] = coleta_valor(navegador, VAR['xpath_preco_gasolina'])
        precos_vbr['cif_s10'] = coleta_valor(navegador, VAR['xpath_preco_s10'])
        precos_vbr['cif_s500'] = coleta_valor(navegador, VAR['xpath_preco_s500'])

    tempo_execucao = round(time() - inicio, 2)

    return precos_vbr, tempo_execucao


if __name__ == "__main__":

    precos_vbr, tempo_execucao = coleta_precos(maximizado=True)

    print("\n----------------------------------")
    print(f"                CIF           FOB       ({tempo_execucao}s)")
    print("Preços Vibra Janjão:")
    print(f"Etanol         {precos_vbr['cif_etanol']}       {precos_vbr['fob_etanol']}")
    print(f"Gasolina       {precos_vbr['cif_gasolina']}       {precos_vbr['fob_gasolina']}")
    print(f"s10            {precos_vbr['cif_s10']}       {precos_vbr['fob_s10']}")
    print(f"s500           {precos_vbr['cif_s500']}       {precos_vbr['fob_s500']}")
    print("----------------------------------")
