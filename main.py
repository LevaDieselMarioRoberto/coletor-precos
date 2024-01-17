from datetime import datetime
from posto import Posto
from coletores_precos.coletor_ipiranga_trr import ColetorIpirangaTRR
from coletores_precos.coletor_vibra_trr import ColetorVibraTRR
from coletores_precos.coletor_raizen_trr import ColetorRaizenTRR
from coletores_precos.coletor_vibra_janjao import ColetorVibraJanjao
from coletores_precos.coletor_ipiranga_postos import ColetorIpirangaPostos
from planilha import Planilha
from logger import Logger
from telegram import Telegram
from concurrent.futures import ThreadPoolExecutor
from time import time

if datetime.now().hour < 20:

    ipr_trr1 = Posto("Ipiranga TRR 1")
    ipr_trr2 = Posto("Ipiranga TRR 2")
    vbr_trr = Posto("Vibra TRR")
    rzn_trr = Posto("Raízen TRR")
    ipr_gasstation = Posto("Ipiranga Gas Station")
    ipr_distrito = Posto("Ipiranga Distrito")
    ipr_itirapua = Posto("Ipiranga Itirapuã")
    ipr_ppp = Posto("Ipiranga PPP")
    ipr_pitstop = Posto("Ipiranga Pit Stop")
    vbr_jj = Posto("Vibra Janjão")

    coletor_ipr_trr = ColetorIpirangaTRR()
    coletor_vbr_trr = ColetorVibraTRR()
    coletor_rzn_trr = ColetorRaizenTRR()
    coletor_ipr_postos = ColetorIpirangaPostos()
    coletor_vbr_jj = ColetorVibraJanjao()

    logger = Logger()
    telegram = Telegram()

    funcoes_e_argumentos = [    # Lista de tuplas, sendo a função e seus respectivos argumentos
        (coletor_ipr_trr.coleta_precos, [ipr_trr1, ipr_trr2]),
        (coletor_vbr_trr.coleta_precos, [vbr_trr]),
        (coletor_rzn_trr.coleta_precos, [rzn_trr]),
        (coletor_vbr_jj.coleta_precos, [vbr_jj]),
        (coletor_ipr_postos.coleta_precos, [ipr_gasstation, ipr_distrito, ipr_itirapua, ipr_ppp, ipr_pitstop]),
    ]

    inicio = time()
    logger.log(f"   --- Iniciando coletas... ---")

    with ThreadPoolExecutor() as executor:  # Executa as funções simultaneamente
        executor.map(lambda x: x[0](*x[1]), funcoes_e_argumentos)

    tempo_total = round(time() - inicio, 2)
    logger.log(f"Tempo de execução: {tempo_total} segundos")

    postos = [ipr_pitstop, ipr_distrito, ipr_gasstation, ipr_itirapua, ipr_ppp, vbr_jj, ipr_trr1, ipr_trr2, vbr_trr, rzn_trr,]
    # for posto in postos: posto.imprime_precos()

    planilha = Planilha()
    planilha.salva_planilha(postos)

    for posto in postos: posto.compara_precos()
