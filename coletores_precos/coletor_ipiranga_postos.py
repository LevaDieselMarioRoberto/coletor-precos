from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config import VAR_IPR_POSTOS as VAR


class ColetorIpirangaPostos(ColetorDePreco):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, ipr_gasstation:Posto, ipr_distrito:Posto, ipr_itirapua:Posto, ipr_ppp:Posto, ipr_pitstop:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Ipiranga (Postos).
        """
        tentativa = 1
        max_tentativas = 3
        nome_portal = "Ipiranga (Postos)"
        prefixo = "IPRPST"
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
                self.clica_botao(VAR['xpath_button_cookies'])
                logger.log(f"{prefixo} - Login realizado com sucesso")

                self.seleciona_filial()                                     # Gás Station
                ipr_gasstation.cif_etanol = self.coleta_valor( VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_gasstation.fob_etanol = self.coleta_valor( VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_gasstation.cif_gasolina = self.coleta_valor( VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_gasstation.fob_gasolina = self.coleta_valor( VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_gasstation.cif_gasolina_ad = self.coleta_valor( VAR['id_preco_cif_gasolinaadt'], xpath_ou_id='id')
                ipr_gasstation.fob_gasolina_ad = self.coleta_valor( VAR['id_preco_fob_gasolinaadt'], xpath_ou_id='id')
                ipr_gasstation.cif_s10 = self.coleta_valor( VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_gasstation.fob_s10 = self.coleta_valor( VAR['id_preco_fob_s10'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços do Gás Station realizada com sucesso")

                self.seleciona_filial(VAR['xpath_button_distrito'])    # Distrito
                ipr_distrito.cif_etanol = self.coleta_valor(VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_distrito.fob_etanol = self.coleta_valor(VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_distrito.cif_gasolina = self.coleta_valor(VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_distrito.fob_gasolina = self.coleta_valor(VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_distrito.cif_s10 = self.coleta_valor(VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_distrito.fob_s10 = self.coleta_valor(VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipr_distrito.cif_s500 = self.coleta_valor(VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipr_distrito.fob_s500 = self.coleta_valor(VAR['id_preco_fob_s500'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços do Distrito realizada com sucesso")

                self.seleciona_filial(VAR['xpath_button_itirapua'])    # Itirapuã
                ipr_itirapua.cif_etanol = self.coleta_valor(VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_itirapua.fob_etanol = self.coleta_valor(VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_itirapua.cif_gasolina = self.coleta_valor(VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_itirapua.fob_gasolina = self.coleta_valor(VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_itirapua.cif_s10 = self.coleta_valor(VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_itirapua.fob_s10 = self.coleta_valor(VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipr_itirapua.cif_s500 = self.coleta_valor(VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipr_itirapua.fob_s500 = self.coleta_valor(VAR['id_preco_fob_s500'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços de Itirapuã realizada com sucesso")

                self.seleciona_filial(VAR['xpath_button_ppp'])         # PPP
                ipr_ppp.cif_etanol = self.coleta_valor(VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_ppp.fob_etanol = self.coleta_valor(VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_ppp.cif_gasolina = self.coleta_valor(VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_ppp.fob_gasolina = self.coleta_valor(VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_ppp.cif_s10 = self.coleta_valor(VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_ppp.fob_s10 = self.coleta_valor(VAR['id_preco_fob_s10'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços do PPP realizada com sucesso")

                self.seleciona_filial(VAR['xpath_button_pitstop'])     # Pit Stop
                ipr_pitstop.cif_etanol = self.coleta_valor(VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_pitstop.fob_etanol = self.coleta_valor(VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_pitstop.cif_gasolina = self.coleta_valor(VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_pitstop.fob_gasolina = self.coleta_valor(VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_pitstop.cif_gasolina_ad = self.coleta_valor(VAR['id_preco_cif_gasolinaadt'], xpath_ou_id='id')
                ipr_pitstop.fob_gasolina_ad = self.coleta_valor(VAR['id_preco_fob_gasolinaadt'], xpath_ou_id='id')
                ipr_pitstop.cif_s10 = self.coleta_valor(VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_pitstop.fob_s10 = self.coleta_valor(VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipr_pitstop.cif_s500 = self.coleta_valor(VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipr_pitstop.fob_s500 = self.coleta_valor(VAR['id_preco_fob_s500'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços do Pit Stop realizada com sucesso")

                self.fechar_navegador()
                self.tempo_execucao = round(time() - self.inicio, 2)
                logger.log(f"{prefixo} - Coleta de preços da {nome_portal} realizada com sucesso")
                logger.log(f"{prefixo} - Tempo de execução: {self.tempo_execucao}s")

                if self.esta_com_erro(prefixo): telegram.enviar_mensagem(f"Coleta de preços da {nome_portal} normalizada 😎")
                break

            except Exception as e:
                tentativa += 1
                self.fechar_navegador()

                if tentativa <= max_tentativas:
                    logger.log_error(f"{prefixo} - Erro na coleta de preços da {nome_portal}")
                    logger.log_error(f"{prefixo} - Nova tentativa de coleta em 30 segundos...")
                    sleep(30)
                    continue
                else:
                    if self.esta_com_erro(prefixo, e): pass
                    else: telegram.enviar_mensagem(f"Erro na coleta de preços da {nome_portal} 😕")
                    logger.log_error(f"{prefixo} - Coleta de preços da {nome_portal} não realizada!")
                    logger.log_error(f"{prefixo} - Erro: {e}")
                    break

    def seleciona_filial(self, filial=''):
        """
        Seleciona uma filial (posto) específica no menu suspenso.
        """
        self.navegador.get(VAR['link_pedidos'])
        sleep(3)

        if str(filial) != '':
            self.clica_botao(VAR['xpath_button_razaosocial'])
            self.clica_botao(filial)
            self.navegador.get(VAR['link_pedidos'])
            sleep(2)

        self.troca_iframe(VAR['xpath_iframe'])
