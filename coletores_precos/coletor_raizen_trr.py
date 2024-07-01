from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config.config_rzn_trr import VAR
import openpyxl


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
                wb = openpyxl.load_workbook(arquivo)
                sheet = wb.active

                raizen_trr.cif_s10 = round(float(str(sheet['B2'].value).replace(",", ".")),4)
                raizen_trr.fob_s10 = round(float(str(sheet['C2'].value).replace(",", ".")),4)
                raizen_trr.cif_s500 = round(float(str(sheet['B3'].value).replace(",", ".")),4)
                raizen_trr.fob_s500 = round(float(str(sheet['C3'].value).replace(",", ".")),4)
                
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
                    logger.log_error(f"{prefixo} - Leitura de preços da {nome_portal} não realizada!")
                    logger.log_error(f"{prefixo} - Erro: {e}")
                    break

    def coleta_precos_disabled(self, raizen_trr:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Raizen (TRR).

        Função desativada após solicitação do portal para verificação via e-mail.
        Coleta passou a ser realizada via Microsoft Power Automate.
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
                logger.log(f"{prefixo} - Iniciando coleta de preços da {nome_portal} (tentativa {tentativa}/{max_tentativas})")
                self.navegador = self.inicializa_navegador(maximizado)
                self.inicio = time()

                # Login na página principal
                self.navegador.get(VAR['link'])
                self.preenche_input(VAR['xpath_input_login'], VAR['login'])
                self.preenche_input(VAR['xpath_input_senha'], VAR['senha'])
                self.clica_botao(VAR['xpath_button_entrar'])
                sleep(3)
                self.navegador.get(VAR['link_precos'])     # Acessa a página de preços
                logger.log(f"{prefixo} - Login e acesso a página de pedidos realizados com sucesso")
                sleep(10)

                # Coleta os preços
                raizen_trr.cif_s10 = self.coleta_valor(VAR['xpath_preco_cif_s10'])
                raizen_trr.fob_s10 = self.coleta_valor(VAR['xpath_preco_fob_s10'])
                raizen_trr.cif_s500 = self.coleta_valor(VAR['xpath_preco_cif_s500'])
                raizen_trr.fob_s500 = self.coleta_valor(VAR['xpath_preco_fob_s500'])

                self.fechar_navegador()
                self.tempo_execucao = round(time() - self.inicio, 2)
                logger.log(f"{prefixo} - Coleta de preços da finalizada - {nome_portal}. Tempo de execução: {self.tempo_execucao}s")

                if self.estava_com_erro(prefixo): telegram.enviar_mensagem(f"Coleta de preços em {nome_portal} normalizada 😎")
                break

            except Exception as e:
                tentativa += 1
                self.fechar_navegador()

                if tentativa <= max_tentativas:
                    logger.log_error(f"{prefixo} - Erro na coleta em {nome_portal}. Nova tentativa em {tempo_espera}s...")
                    sleep(tempo_espera)
                    continue
                else:
                    if self.eh_terceiro_erro_consecutivo(prefixo, e):
                        telegram.enviar_mensagem(f"Erro na coleta de preços da {nome_portal} 😕")

                    logger.log_error(f"{prefixo} - Coleta de preços da {nome_portal}. Erro: {e}")
                    break
