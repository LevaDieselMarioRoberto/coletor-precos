import ipiranga
import vibra
import raizen
from time import time
from concurrent.futures import ThreadPoolExecutor

def coleta_e_imprime_precos(empresa):
    preco_fob_s10, preco_fob_s500, preco_cif_s10, preco_cif_s500, tempo_ex = empresa.coleta_precos()
    
    print("Preços", empresa.__name__, ":")
    print("FOB S10 ...:", preco_fob_s10)
    print("FOB S500 ..:", preco_fob_s500)
    print("CIF S10 ...:", preco_cif_s10)
    print("CIF S500 ..:", preco_cif_s500)
    print("Tempo de coleta:", tempo_ex, "segundos\n")

if __name__ == "__main__":
    empresas = [ipiranga, vibra, raizen]
    
    inicio = time()
    
    with ThreadPoolExecutor(max_workers=len(empresas)) as executor:
        executor.map(coleta_e_imprime_precos, empresas)
    
    print("Tempo total: " + str(round(time() - inicio, 2)) + " segundos")
