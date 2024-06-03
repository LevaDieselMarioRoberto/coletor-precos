from datetime import datetime
from posto import Posto
from coletores_precos.coletor_ipiranga_trr import ColetorIpirangaTRR
from coletores_precos.coletor_vibra_trr import ColetorVibraTRR
from coletores_precos.coletor_raizen_trr import ColetorRaizenTRR
from coletores_precos.coletor_vibra_janjao import ColetorVibraJanjao
from coletores_precos.coletor_ipiranga_postos import ColetorIpirangaPostos
from planilha import Planilha
from logger import Logger
from concurrent.futures import ThreadPoolExecutor
from time import time
from config import CONTROLS


logger = Logger()

if CONTROLS['COLETA_HABILITADA'] and datetime.now().hour < 20:

    funcoes_e_argumentos = [] # Lista de tuplas, sendo a função e seus respectivos argumentos

    if CONTROLS['COLETAR_IPR_TRR']:
        ipr_trr1 = Posto("Ipiranga TRR 1")
        ipr_trr2 = Posto("Ipiranga TRR 2")
        coletor_ipr_trr = ColetorIpirangaTRR()
        funcoes_e_argumentos.append((
            coletor_ipr_trr.coleta_precos,
            [ipr_trr1, ipr_trr2, CONTROLS['MAXIMIZADO_IPR_TRR']]
        ))
    
    if CONTROLS['COLETAR_VBR_TRR']:
        vbr_trr = Posto("Vibra TRR")
        coletor_vbr_trr = ColetorVibraTRR()
        funcoes_e_argumentos.append((
            coletor_vbr_trr.coleta_precos,
            [vbr_trr, CONTROLS['MAXIMIZADO_VBR_TRR']]
        ))

    if CONTROLS['COLETAR_RZN_TRR']:
        rzn_trr = Posto("Raízen TRR")
        coletor_rzn_trr = ColetorRaizenTRR()
        funcoes_e_argumentos.append((
            coletor_rzn_trr.coleta_precos,
            [rzn_trr, CONTROLS['MAXIMIZADO_RZN_TRR']]
        ))

    if CONTROLS['COLETAR_IPR_POSTOS']:
        ipr_gasstation = Posto("Ipiranga Gas Station")
        ipr_distrito = Posto("Ipiranga Distrito")
        ipr_itirapua = Posto("Ipiranga Itirapuã")
        ipr_ppp = Posto("Ipiranga PPP")
        ipr_pitstop = Posto("Ipiranga Pit Stop")
        coletor_ipr_postos = ColetorIpirangaPostos()
        funcoes_e_argumentos.append((
            coletor_ipr_postos.coleta_precos,
            [ipr_gasstation, ipr_distrito, ipr_itirapua, ipr_ppp, ipr_pitstop, CONTROLS['MAXIMIZADO_IPR_POSTOS']]
        ))
    
    if CONTROLS['COLETAR_VBR_JJ']:
        vbr_jj = Posto("Vibra Janjão")
        coletor_vbr_jj = ColetorVibraJanjao()
        funcoes_e_argumentos.append((
            coletor_vbr_jj.coleta_precos,
            [vbr_jj, CONTROLS['MAXIMIZADO_VBR_JJ']]
        ))

    inicio = time()
    logger.log(f"   --- Iniciando coletas... ---")

    with ThreadPoolExecutor() as executor:  # Executa as funções simultaneamente
        executor.map(lambda x: x[0](*x[1]), funcoes_e_argumentos)

    tempo_total = round(time() - inicio, 2)
    logger.log(f"Tempo de execução: {tempo_total} segundos")

    postos = []

    if CONTROLS['COLETAR_IPR_POSTOS']: postos.extend([ipr_gasstation, ipr_distrito, ipr_itirapua, ipr_ppp, ipr_pitstop])
    if CONTROLS['COLETAR_VBR_JJ']: postos.append(vbr_jj)
    if CONTROLS['COLETAR_IPR_TRR']: postos.extend([ipr_trr1, ipr_trr2])
    if CONTROLS['COLETAR_VBR_TRR']: postos.append(vbr_trr)
    if CONTROLS['COLETAR_RZN_TRR']: postos.append(rzn_trr)

    if CONTROLS['IMPRIME_PRECOS_TERMINAL']:
        for posto in postos: posto.imprime_precos()

    if CONTROLS['SALVA_PRECOS_PLANILHA']:
        planilha = Planilha()
        planilha.salva_planilha(postos)

    if CONTROLS['ENVIA_PRECOS_TELEGRAM']:
        for posto in postos: posto.compara_precos()

else:
    logger.log("Coleta desabilitada ou fora do horário permitido.")
