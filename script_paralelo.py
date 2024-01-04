import threading
import ipiranga
import vibra
import raizen
import ipiranga_postos
import vibra_janjao
from time import time

global precos_ipr1, precos_ipr2, precos_vbr, precos_rzn, tempo_ex_ipr, tempo_ex_vbr, tempo_ex_rzn
global precos_gasstation, precos_distrito, precos_itirapua, precos_ppp, precos_pitstop, tempo_ex_ipr_postos
global precos_vbr_janjao, tempo_ex_vbr_janjao


def coleta_e_imprime(preco_func, nome_posto):
    
    global precos_ipr1, precos_ipr2, precos_vbr, precos_rzn, tempo_ex_ipr, tempo_ex_vbr, tempo_ex_rzn
    global precos_gasstation, precos_distrito, precos_itirapua, precos_ppp, precos_pitstop, tempo_ex_ipr_postos
    global precos_vbr_janjao, tempo_ex_vbr_janjao

    if nome_posto == "Ipiranga":
        precos_ipr1, precos_ipr2, tempo_ex_ipr = preco_func()
    elif nome_posto == "Vibra":
        precos_vbr, tempo_ex_vbr = preco_func()
    elif nome_posto == "Raizen":
        precos_rzn, tempo_ex_rzn = preco_func()
    elif nome_posto == "Ipiranga Postos":
        precos_gasstation, precos_distrito, precos_itirapua, precos_ppp, precos_pitstop, tempo_ex_ipr_postos = preco_func()
    elif nome_posto == "Vibra Janjão":
        precos_vbr_janjao, tempo_ex_vbr_janjao = preco_func()


inicio = time()

# Criando as threads para coletar os preços em paralelo
thread_ipr = threading.Thread(target=coleta_e_imprime, args=(ipiranga.coleta_precos, "Ipiranga"))
thread_vbr = threading.Thread(target=coleta_e_imprime, args=(vibra.coleta_precos, "Vibra"))
thread_rzn = threading.Thread(target=coleta_e_imprime, args=(raizen.coleta_precos, "Raizen"))
thread_ipr_postos = threading.Thread(target=coleta_e_imprime, args=(ipiranga_postos.coleta_precos, "Ipiranga Postos"))
thread_vbr_janjao = threading.Thread(target=coleta_e_imprime, args=(vibra_janjao.coleta_precos, "Vibra Janjão"))

# Iniciando as threads
thread_ipr.start()
thread_vbr.start()
thread_rzn.start()
thread_ipr_postos.start()
thread_vbr_janjao.start()

# Aguardando as threads terminarem
thread_ipr.join()
thread_vbr.join()
thread_rzn.join()
thread_ipr_postos.join()
thread_vbr_janjao.join()

print("\n----------------------------------")
print("                CIF           FOB\n")

print("TRR:\n")

print(f"Ipiranga [1]:              ({tempo_ex_ipr}s)")
print(f"s10            {precos_ipr1['cif_s10']}       {precos_ipr1['fob_s10']}")
print(f"s500           {precos_ipr1['cif_s500']}       {precos_ipr1['fob_s500']}")
print(f"Ipiranga [2]:")
print(f"s10            {precos_ipr2['cif_s10']}       {precos_ipr2['fob_s10']}")
print(f"s500           {precos_ipr2['cif_s500']}       {precos_ipr2['fob_s500']}\n")

print(f"Vibra:                     ({tempo_ex_vbr}s)")
print(f"s10            {precos_vbr['cif_s10']}       {precos_vbr['fob_s10']}")
print(f"s500           {precos_vbr['cif_s500']}       {precos_vbr['fob_s500']}\n")

print(f"Raizen:                    ({tempo_ex_rzn}s)")
print(f"s10            {precos_rzn['cif_s10']}       {precos_rzn['fob_s10']}")
print(f"s500           {precos_rzn['cif_s500']}       {precos_rzn['fob_s500']}\n")

print("\nPostos:\n")

print(f"Ipiranga Gás Station:      ({tempo_ex_ipr_postos}s)")
print(f"Etanol         {precos_gasstation['cif_etanol']}       {precos_gasstation['fob_etanol']}")
print(f"Gasolina       {precos_gasstation['cif_gasolina']}       {precos_gasstation['fob_gasolina']}")
print(f"Gasolina Ad    {precos_gasstation['cif_gasolina_adt']}       {precos_gasstation['fob_gasolina_adt']}")
print(f"s10            {precos_gasstation['cif_s10']}       {precos_gasstation['fob_s10']}\n")

print("Ipiranga Distrito:")
print(f"Etanol         {precos_distrito['cif_etanol']}       {precos_distrito['fob_etanol']}")
print(f"Gasolina       {precos_distrito['cif_gasolina']}       {precos_distrito['fob_gasolina']}")
print(f"s10            {precos_distrito['cif_s10']}       {precos_distrito['fob_s10']}")
print(f"s500           {precos_distrito['cif_s500']}       {precos_distrito['fob_s500']}\n")

print("Ipiranga Itirapuã:")
print(f"Etanol         {precos_itirapua['cif_etanol']}       {precos_itirapua['fob_etanol']}")
print(f"Gasolina       {precos_itirapua['cif_gasolina']}       {precos_itirapua['fob_gasolina']}")
print(f"s10            {precos_itirapua['cif_s10']}       {precos_itirapua['fob_s10']}")
print(f"s500           {precos_itirapua['cif_s500']}       {precos_itirapua['fob_s500']}\n")

print("Ipiranga PPP:")
print(f"Etanol         {precos_ppp['cif_etanol']}       {precos_ppp['fob_etanol']}")
print(f"Gasolina       {precos_ppp['cif_gasolina']}       {precos_ppp['fob_gasolina']}")
print(f"s10            {precos_ppp['cif_s10']}       {precos_ppp['fob_s10']}\n")

print("Ipiranga Pit Stop:")
print(f"Etanol         {precos_pitstop['cif_etanol']}       {precos_pitstop['fob_etanol']}")
print(f"Gasolina       {precos_pitstop['cif_gasolina']}       {precos_pitstop['fob_gasolina']}")
print(f"Gasolina Ad    {precos_pitstop['cif_gasolina_adt']}       {precos_pitstop['fob_gasolina_adt']}")
print(f"s10            {precos_pitstop['cif_s10']}       {precos_pitstop['fob_s10']}")
print(f"s500           {precos_pitstop['cif_s500']}       {precos_pitstop['fob_s500']}\n")

print(f"Vibra Janjão:              ({tempo_ex_vbr_janjao}s)")
print(f"Etanol         {precos_vbr_janjao['cif_etanol']}       {precos_vbr_janjao['fob_etanol']}")
print(f"Gasolina       {precos_vbr_janjao['cif_gasolina']}       {precos_vbr_janjao['fob_gasolina']}")
print(f"s10            {precos_vbr_janjao['cif_s10']}       {precos_vbr_janjao['fob_s10']}")
print(f"s500           {precos_vbr_janjao['cif_s500']}       {precos_vbr_janjao['fob_s500']}\n")

print(f"Tempo total: {round(time() - inicio, 2)} segundos")
print("----------------------------------")
