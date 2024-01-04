import threading
import ipiranga
import vibra
import raizen
from time import time

global precos_ipr1, precos_ipr2, precos_vbr, precos_rzn, tempo_ex_ipr, tempo_ex_vbr, tempo_ex_rzn


def coleta_e_imprime(preco_func, nome_posto):
    
    global precos_ipr1, precos_ipr2, precos_vbr, precos_rzn, tempo_ex_ipr, tempo_ex_vbr, tempo_ex_rzn

    if nome_posto == "Ipiranga":
        precos_ipr1, precos_ipr2, tempo_ex_ipr = preco_func()
    elif nome_posto == "Vibra":
        precos_vbr, tempo_ex_vbr = preco_func()
    elif nome_posto == "Raizen":
        precos_rzn, tempo_ex_rzn = preco_func()


inicio = time()

# Criando as threads para coletar os preços em paralelo
thread_ipr = threading.Thread(target=coleta_e_imprime, args=(ipiranga.coleta_precos, "Ipiranga"))
thread_vbr = threading.Thread(target=coleta_e_imprime, args=(vibra.coleta_precos, "Vibra"))
thread_rzn = threading.Thread(target=coleta_e_imprime, args=(raizen.coleta_precos, "Raizen"))

# Iniciando as threads
thread_ipr.start()
thread_vbr.start()
thread_rzn.start()

# Aguardando as threads terminarem
thread_ipr.join()
thread_vbr.join()
thread_rzn.join()

print("\n----------------------------------")
print("            CIF           FOB\n")

print(f"Ipiranga [1]:              ({tempo_ex_ipr}s)")
print(f"s10        {precos_ipr1['cif_s10']}       {precos_ipr1['fob_s10']}")
print(f"s500       {precos_ipr1['cif_s500']}       {precos_ipr1['fob_s500']}")
print(f"Ipiranga [2]:")
print(f"s10        {precos_ipr2['cif_s10']}       {precos_ipr2['fob_s10']}")
print(f"s500       {precos_ipr2['cif_s500']}       {precos_ipr2['fob_s500']}\n")

print(f"Vibra:                     ({tempo_ex_vbr}s)")
print(f"s10        {precos_vbr['cif_s10']}       {precos_vbr['fob_s10']}")
print(f"s500       {precos_vbr['cif_s500']}       {precos_vbr['fob_s500']}\n")

print(f"Raizen:                    ({tempo_ex_rzn}s)")
print(f"s10        {precos_rzn['cif_s10']}       {precos_rzn['fob_s10']}")
print(f"s500       {precos_rzn['cif_s500']}       {precos_rzn['fob_s500']}\n")

print(f"Tempo total: {str(round(time() - inicio, 2))} segundos")
print("----------------------------------")
