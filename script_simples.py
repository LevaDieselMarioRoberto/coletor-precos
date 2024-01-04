import ipiranga
import vibra
import raizen
from time import time

inicio = time()

precos_ipr1, precos_ipr2, tempo_ex_ipr = ipiranga.coleta_precos()
precos_vbr, tempo_ex_vbr = vibra.coleta_precos()
precos_rzn, tempo_ex_rzn = raizen.coleta_precos()

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

print("Tempo total: " + str(round(time() - inicio, 2)) + " segundos")
print("----------------------------------")
