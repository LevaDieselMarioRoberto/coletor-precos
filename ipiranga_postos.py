from config import var_ipr_postos as VAR
from funcoes import inicializa_navegador, clica_botao, preenche_input, coleta_valor, troca_iframe
from time import sleep, time

def coleta_precos(maximizado=False):
    """
    Coleta preços de produtos em uma página da web usando Selenium.

    Args:
        maximizado (bool): Indica se a janela do navegador deve ser maximizada (padrão é False).

    Returns:
        tuple: Um tupla contendo dicionários de preços para diferentes postos e o tempo de execução.
    """

    inicio = time()
    navegador = inicializa_navegador(maximizado)

    def seleciona_filial(navegador, filial=''):
        """
        Seleciona uma filial (posto) específica no menu suspenso.

        Args:
            navegador: O objeto do navegador Selenium.
            filial (str): O nome da filial a ser selecionada (padrão é vazio para a filial padrão).
        """

        navegador.get(VAR['link_pedidos'])
        sleep(3)

        if str(filial) != '':
            clica_botao(navegador, VAR['xpath_button_razaosocial'])
            clica_botao(navegador, filial)
            navegador.get(VAR['link_pedidos'])
            sleep(2)

        troca_iframe(navegador, VAR['xpath_iframe'])


    with navegador:

        # Login na página principal
        navegador.get(VAR['link'])
        preenche_input(navegador, VAR['xpath_input_login'], VAR['login'])
        preenche_input(navegador, VAR['xpath_input_senha'], VAR['senha'])
        clica_botao(navegador, VAR['xpath_button_entrar'])
        clica_botao(navegador, VAR['xpath_button_cookies'])

        seleciona_filial(navegador)  # Gás Station
        precos_gasstation = {}
        precos_gasstation['cif_etanol'] = coleta_valor(navegador, VAR['id_preco_cif_etanol'], xpath_ou_id='id')
        precos_gasstation['fob_etanol'] = coleta_valor(navegador, VAR['id_preco_fob_etanol'], xpath_ou_id='id')
        precos_gasstation['cif_gasolina'] = coleta_valor(navegador, VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
        precos_gasstation['fob_gasolina'] = coleta_valor(navegador, VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
        precos_gasstation['cif_gasolina_adt'] = coleta_valor(navegador, VAR['id_preco_cif_gasolinaadt'], xpath_ou_id='id')
        precos_gasstation['fob_gasolina_adt'] = coleta_valor(navegador, VAR['id_preco_fob_gasolinaadt'], xpath_ou_id='id')
        precos_gasstation['cif_s10'] = coleta_valor(navegador, VAR['id_preco_cif_s10'], xpath_ou_id='id')
        precos_gasstation['fob_s10'] = coleta_valor(navegador, VAR['id_preco_fob_s10'], xpath_ou_id='id')

        seleciona_filial(navegador, VAR['xpath_button_distrito']) # Distrito
        precos_distrito = {}
        precos_distrito['cif_etanol'] = coleta_valor(navegador, VAR['id_preco_cif_etanol'], xpath_ou_id='id')
        precos_distrito['fob_etanol'] = coleta_valor(navegador, VAR['id_preco_fob_etanol'], xpath_ou_id='id')
        precos_distrito['cif_gasolina'] = coleta_valor(navegador, VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
        precos_distrito['fob_gasolina'] = coleta_valor(navegador, VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
        precos_distrito['cif_s10'] = coleta_valor(navegador, VAR['id_preco_cif_s10'], xpath_ou_id='id')
        precos_distrito['fob_s10'] = coleta_valor(navegador, VAR['id_preco_fob_s10'], xpath_ou_id='id')
        precos_distrito['cif_s500'] = coleta_valor(navegador, VAR['id_preco_cif_s500'], xpath_ou_id='id')
        precos_distrito['fob_s500'] = coleta_valor(navegador, VAR['id_preco_fob_s500'], xpath_ou_id='id')

        seleciona_filial(navegador, VAR['xpath_button_itirapua']) # Itirapuã
        precos_itirapua = {}
        precos_itirapua['cif_etanol'] = coleta_valor(navegador, VAR['id_preco_cif_etanol'], xpath_ou_id='id')
        precos_itirapua['fob_etanol'] = coleta_valor(navegador, VAR['id_preco_fob_etanol'], xpath_ou_id='id')
        precos_itirapua['cif_gasolina'] = coleta_valor(navegador, VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
        precos_itirapua['fob_gasolina'] = coleta_valor(navegador, VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
        precos_itirapua['cif_s10'] = coleta_valor(navegador, VAR['id_preco_cif_s10'], xpath_ou_id='id')
        precos_itirapua['fob_s10'] = coleta_valor(navegador, VAR['id_preco_fob_s10'], xpath_ou_id='id')
        precos_itirapua['cif_s500'] = coleta_valor(navegador, VAR['id_preco_cif_s500'], xpath_ou_id='id')
        precos_itirapua['fob_s500'] = coleta_valor(navegador, VAR['id_preco_fob_s500'], xpath_ou_id='id')

        seleciona_filial(navegador, VAR['xpath_button_ppp']) # PPP
        precos_ppp = {}
        precos_ppp['cif_etanol'] = coleta_valor(navegador, VAR['id_preco_cif_etanol'], xpath_ou_id='id')
        precos_ppp['fob_etanol'] = coleta_valor(navegador, VAR['id_preco_fob_etanol'], xpath_ou_id='id')
        precos_ppp['cif_gasolina'] = coleta_valor(navegador, VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
        precos_ppp['fob_gasolina'] = coleta_valor(navegador, VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
        precos_ppp['cif_s10'] = coleta_valor(navegador, VAR['id_preco_cif_s10'], xpath_ou_id='id')
        precos_ppp['fob_s10'] = coleta_valor(navegador, VAR['id_preco_fob_s10'], xpath_ou_id='id')

        seleciona_filial(navegador, VAR['xpath_button_pitstop']) # Pit Stop
        precos_pitstop = {}
        precos_pitstop['cif_etanol'] = coleta_valor(navegador, VAR['id_preco_cif_etanol'], xpath_ou_id='id')
        precos_pitstop['fob_etanol'] = coleta_valor(navegador, VAR['id_preco_fob_etanol'], xpath_ou_id='id')
        precos_pitstop['cif_gasolina'] = coleta_valor(navegador, VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
        precos_pitstop['fob_gasolina'] = coleta_valor(navegador, VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
        precos_pitstop['cif_gasolina_adt'] = coleta_valor(navegador, VAR['id_preco_cif_gasolinaadt'], xpath_ou_id='id')
        precos_pitstop['fob_gasolina_adt'] = coleta_valor(navegador, VAR['id_preco_fob_gasolinaadt'], xpath_ou_id='id')
        precos_pitstop['cif_s10'] = coleta_valor(navegador, VAR['id_preco_cif_s10'], xpath_ou_id='id')
        precos_pitstop['fob_s10'] = coleta_valor(navegador, VAR['id_preco_fob_s10'], xpath_ou_id='id')
        precos_pitstop['cif_s500'] = coleta_valor(navegador, VAR['id_preco_cif_s500'], xpath_ou_id='id')
        precos_pitstop['fob_s500'] = coleta_valor(navegador, VAR['id_preco_fob_s500'], xpath_ou_id='id')

    tempo_execucao = round(time() - inicio, 2)

    return precos_gasstation, precos_distrito, precos_itirapua, precos_ppp, precos_pitstop, tempo_execucao


if __name__ == "__main__":

    precos_gasstation, precos_distrito, precos_itirapua, precos_ppp, precos_pitstop, tempo_execucao = coleta_precos(maximizado=True)

    print("\n----------------------------------")
    print("                CIF           FOB")
    print(f"Preços Ipiranga                                    ({tempo_execucao}s)\n")
    print("Gás Station:")
    print(f"Etanol         {precos_gasstation['cif_etanol']}       {precos_gasstation['fob_etanol']}")
    print(f"Gasolina       {precos_gasstation['cif_gasolina']}       {precos_gasstation['fob_gasolina']}")
    print(f"Gasolina Ad    {precos_gasstation['cif_gasolina_adt']}       {precos_gasstation['fob_gasolina_adt']}")
    print(f"s10            {precos_gasstation['cif_s10']}       {precos_gasstation['fob_s10']}\n")
    print("Distrito:")
    print(f"Etanol         {precos_distrito['cif_etanol']}       {precos_distrito['fob_etanol']}")
    print(f"Gasolina       {precos_distrito['cif_gasolina']}       {precos_distrito['fob_gasolina']}")
    print(f"s10            {precos_distrito['cif_s10']}       {precos_distrito['fob_s10']}")
    print(f"s500           {precos_distrito['cif_s500']}       {precos_distrito['fob_s500']}\n")
    print("Itirapuã:")
    print(f"Etanol         {precos_itirapua['cif_etanol']}       {precos_itirapua['fob_etanol']}")
    print(f"Gasolina       {precos_itirapua['cif_gasolina']}       {precos_itirapua['fob_gasolina']}")
    print(f"s10            {precos_itirapua['cif_s10']}       {precos_itirapua['fob_s10']}")
    print(f"s500           {precos_itirapua['cif_s500']}       {precos_itirapua['fob_s500']}\n")
    print("PPP:")
    print(f"Etanol         {precos_ppp['cif_etanol']}       {precos_ppp['fob_etanol']}")
    print(f"Gasolina       {precos_ppp['cif_gasolina']}       {precos_ppp['fob_gasolina']}")
    print(f"s10            {precos_ppp['cif_s10']}       {precos_ppp['fob_s10']}\n")
    print("Pit Stop:")
    print(f"Etanol         {precos_pitstop['cif_etanol']}       {precos_pitstop['fob_etanol']}")
    print(f"Gasolina       {precos_pitstop['cif_gasolina']}       {precos_pitstop['fob_gasolina']}")
    print(f"Gasolina Ad    {precos_pitstop['cif_gasolina_adt']}       {precos_pitstop['fob_gasolina_adt']}")
    print(f"s10            {precos_pitstop['cif_s10']}       {precos_pitstop['fob_s10']}")
    print(f"s500           {precos_pitstop['cif_s500']}       {precos_pitstop['fob_s500']}")
    print("----------------------------------\n")
