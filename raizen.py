from config import var_rzn as VAR
from funcoes import inicializa_navegador, clica_botao, preenche_input, coleta_valor
from time import sleep, time

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

        sleep(3)
        navegador.get(VAR['link_precos'])   # Acessa a página de preços
        sleep(10)

        precos_rzn = {}     # Coleta preços CIF e FOB
        precos_rzn['cif_s10'] = coleta_valor(navegador, VAR['xpath_preco_cif_s10'])
        precos_rzn['fob_s10'] = coleta_valor(navegador, VAR['xpath_preco_fob_s10'])
        precos_rzn['cif_s500'] = coleta_valor(navegador, VAR['xpath_preco_cif_s500'])
        precos_rzn['fob_s500'] = coleta_valor(navegador, VAR['xpath_preco_fob_s500'])

    tempo_execucao = round(time() - inicio, 2)

    return precos_rzn, tempo_execucao


if __name__ == "__main__":

    precos_rzn, tempo_execucao = coleta_precos(maximizado=True)

    print("\n----------------------------------")
    print(f"                CIF           FOB       ({tempo_execucao}s)")
    print("Preços Raizen TRR:")
    print(f"s10            {round(precos_rzn['cif_s10'], 4)}       {round(precos_rzn['fob_s10'], 4)}")
    print(f"s500           {round(precos_rzn['cif_s500'], 4)}       {round(precos_rzn['fob_s500'], 4)}")
    print("----------------------------------")
