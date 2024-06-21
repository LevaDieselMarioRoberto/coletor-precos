from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config.config_vbr_janjao import VAR


class ColetorVibraJanjao(ColetorDePreco):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, vbr_jj:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Vibra (Janjão).
        """
        tentativa = 1
        max_tentativas = int(VAR['tentativas'])
        tempo_espera = int(VAR['espera_se_erro'])
        nome_portal = "Vibra (Janjão)"
        prefixo = "VBRJJ"
        logger = Logger()
        telegram = Telegram()

        while tentativa <= max_tentativas:
            try:
                logger.log(f"{prefixo} - Iniciando coleta de preços da {nome_portal} (tentativa {tentativa}/{max_tentativas})")
                self.navegador = self.inicializa_navegador(maximizado, browser='firefox')
                self.inicio = time()

                # Login na página principal
                self.navegador.get(VAR['link_pedidos'])
                self.preenche_input(VAR['xpath_input_login'], VAR['login'])
                self.preenche_input(VAR['xpath_input_senha'], VAR['senha'])
                self.clica_botao(VAR['xpath_button_entrar'])
                logger.log(f"{prefixo} - Login realizado com sucesso")

                # Coleta de preços FOB
                sleep(2)
                vbr_jj.fob_etanol = self.coleta_valor(VAR['xpath_preco_etanol'])
                vbr_jj.fob_gasolina = self.coleta_valor(VAR['xpath_preco_gasolina'])
                vbr_jj.fob_s10 = self.coleta_valor(VAR['xpath_preco_s10'])
                vbr_jj.fob_s500 = self.coleta_valor(VAR['xpath_preco_s500'])
                logger.log(f"{prefixo} - Coleta de preços FOB realizada")
                sleep(2)

                # Alteração para modo CIF
                self.muda_modo(VAR['id_select_modo'], VAR['modo'], sleep_time=18)
                logger.log(f"{prefixo} - Modo alterado para CIF")

                # Coleta de preços CIF
                sleep(2)
                vbr_jj.cif_etanol = self.coleta_valor(VAR['xpath_preco_etanol'])
                vbr_jj.cif_gasolina = self.coleta_valor(VAR['xpath_preco_gasolina'])
                vbr_jj.cif_s10 = self.coleta_valor(VAR['xpath_preco_s10'])
                vbr_jj.cif_s500 = self.coleta_valor(VAR['xpath_preco_s500'])
                logger.log(f"{prefixo} - Coleta de preços CIF realizada")
                sleep(2)

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
