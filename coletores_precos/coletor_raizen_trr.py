from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config.config_rzn_trr import VAR
import os


class ColetorRaizenTRR(ColetorDePreco):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, raizen_trr:Posto, maximizado=False):
        """
        Lê preços de s10 e s500 coletados via Power Automate.
        """
        tentativa = 1
        max_tentativas = int(VAR['tentativas'])
        tempo_espera = int(VAR['espera_se_erro'])
        nome_portal = "Raízen (TRR)"
        prefixo = "RZNTRR"
        logger = Logger()
        telegram = Telegram()

        while tentativa <= max_tentativas:
            try:
                logger.log(f"{prefixo} - Iniciando leitura de preços da {nome_portal} (tentativa {tentativa}/{max_tentativas})")
                self.inicio = time()

                arquivo = VAR['precos_power_automate']

                # Verifica se o arquivo TXT existe antes de tentar abri-lo
                if not os.path.isfile(arquivo):
                    raise FileNotFoundError(f"{prefixo} - Arquivo TXT da Raízen não encontrado no caminho: {arquivo}")

                # Verifica se o arquivo TXT não está vazio
                if os.path.getsize(arquivo) == 0:
                    raise ValueError(f"{prefixo} - Arquivo TXT da Raízen está vazio")

                try:
                    with open(arquivo, 'r') as f:
                        linhas = f.readlines()
                    
                    # Remove espaços em branco e quebras de linha das linhas
                    linhas = [linha.strip() for linha in linhas]
                    linhas = [linha.replace("\x00", "") for linha in linhas]
                    linhas = [linha.replace("ÿþ", "") for linha in linhas]
                    linhas.remove('')
                    linhas.remove('')
                    linhas.remove('')
                    logger.log(f"{prefixo} - Linhas do arquivo TXT: {linhas}")
                    
                    # Verifica se há exatamente 4 items na lista
                    if len(linhas) != 4:
                        raise ValueError(f"{prefixo} - O arquivo TXT deve conter exatamente 4 linhas com preços.")

                    # Atribui os valores às variáveis
                    raizen_trr.cif_s10 = round(float(linhas[0]), 4)
                    raizen_trr.fob_s10 = round(float(linhas[1]), 4)
                    raizen_trr.cif_s500 = round(float(linhas[2]), 4)
                    raizen_trr.fob_s500 = round(float(linhas[3]), 4)
                    logger.log(f"{prefixo} - Preços da Raízen (TRR): s10: {raizen_trr.cif_s10}/{raizen_trr.fob_s10}, s500: {raizen_trr.cif_s500}/{raizen_trr.fob_s500}")

                except ValueError as e:
                    logger.log_error(f"{prefixo} - Erro ao converter valores do arquivo TXT: {e}")
                    raise
                except Exception as e:
                    logger.log_error(f"{prefixo} - Erro ao processar o arquivo TXT: {e}")
                    raise
                
                self.tempo_execucao = round(time() - self.inicio, 2)
                logger.log(f"{prefixo} - Leitura de preços da finalizada - {nome_portal}. Tempo de execução: {self.tempo_execucao}s")
                break
            except Exception as e:
                tentativa += 1
                if tentativa <= max_tentativas:
                    logger.log_error(f"{prefixo} - Erro na leitura em {nome_portal}. Nova tentativa em {tempo_espera}s...")
                    sleep(tempo_espera)
                    continue
                else:
                    telegram.enviar_mensagem(f"Erro na coleta de preços da {nome_portal} 😕")
                    logger.log_error(f"{prefixo} - Leitura de preços da {nome_portal} não realizada!")
                    logger.log_error(f"{prefixo} - Erro: {e}")
                    break
