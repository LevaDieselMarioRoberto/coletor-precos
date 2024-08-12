from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config.config_ipr_postos import VAR


class ColetorIpirangaPostos(ColetorDePreco):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, ipr_gasstation:Posto, ipr_distrito:Posto, ipr_itirapua:Posto, ipr_ppp:Posto, ipr_pitstop:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Ipiranga (Postos).
        """
        tentativa = 1
        max_tentativas = int(VAR['tentativas'])
        tempo_espera = int(VAR['espera_se_erro'])
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
                logger.log(f"{prefixo} - Login realizado")

                postos = [ipr_gasstation, ipr_distrito, ipr_itirapua, ipr_ppp, ipr_pitstop]
                nomes = ['Gas Station', 'Distrito', 'Itirapuã', 'PPP', 'Pit Stop']
                xpaths = ['', VAR['xpath_button_distrito'], VAR['xpath_button_itirapua'], VAR['xpath_button_ppp'], VAR['xpath_button_pitstop']]

                for posto, nome, xpath in zip(postos, nomes, xpaths):
                    self.seleciona_filial(xpath)
                    posto.cif_etanol = self.coleta_valor(VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                    posto.fob_etanol = self.coleta_valor(VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                    posto.cif_gasolina = self.coleta_valor(VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                    posto.fob_gasolina = self.coleta_valor(VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                    if nome == 'Pit Stop' or nome == 'Gas Station':
                        posto.cif_gasolina_ad = self.coleta_valor(VAR['id_preco_cif_gasolinaadt'], xpath_ou_id='id')
                        posto.fob_gasolina_ad = self.coleta_valor(VAR['id_preco_fob_gasolinaadt'], xpath_ou_id='id')
                    posto.cif_s10 = self.coleta_valor(VAR['id_preco_cif_s10'], xpath_ou_id='id')
                    posto.fob_s10 = self.coleta_valor(VAR['id_preco_fob_s10'], xpath_ou_id='id')
                    if nome != 'Gas Station' and nome != 'PPP':
                        posto.cif_s500 = self.coleta_valor(VAR['id_preco_cif_s500'], xpath_ou_id='id')
                        posto.fob_s500 = self.coleta_valor(VAR['id_preco_fob_s500'], xpath_ou_id='id')
                    logger.log(f"{prefixo} - Coleta de preços realizada - {nome}")

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
                    # if self.eh_terceiro_erro_consecutivo(prefixo, e):
                    telegram.enviar_mensagem(f"Erro na coleta de preços da {nome_portal} 😕")

                    logger.log_error(f"{prefixo} - Coleta de preços da {nome_portal}. Erro: {e}")
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
            sleep(2)

        self.troca_iframe(VAR['xpath_iframe'])
