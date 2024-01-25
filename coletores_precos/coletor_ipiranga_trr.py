from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config import VAR_IPR_TRR as VAR


class ColetorIpirangaTRR(ColetorDePreco):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, ipiranga_trr1:Posto, ipiranga_trr2:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Ipiranga (TRR).
        """
        tentativa = 1
        max_tentativas = 3
        nome_portal = "Ipiranga (TRR)"
        prefixo = "IPRTRR"
        logger = Logger()
        telegram = Telegram()

        while tentativa <= max_tentativas:
            try:
                logger.log(f"{prefixo} - Inicinando coleta de preços da {nome_portal} (tentativa {tentativa}/{max_tentativas})")
                self.navegador = self.inicializa_navegador(maximizado)
                self.inicio = time()

                # Login na página principal
                self.navegador.get(VAR['link'])
                self.preenche_input(VAR['xpath_input_login'], VAR['login'])
                self.preenche_input(VAR['xpath_input_senha'], VAR['senha'])
                self.clica_botao(VAR['xpath_button_entrar'])
                self.clica_botao(VAR['xpath_button_cookies'])
                self.clica_botao(VAR['xpath_button_pedidos'])
                logger.log(f"{prefixo} - Login e acesso a página de pedidos realizados com sucesso")

                # Troca para o iframe e seleciona a base
                self.troca_iframe(VAR['xpath_iframe'])
                self.seleciona_opcao_menu_suspenso(VAR['xpath_select_base'], VAR['base'])
                logger.log(f"{prefixo} - Troca de iframe e base selecionada com sucesso")

                # Coleta os preços do primeiro perfil da TRR
                ipiranga_trr1.cif_s10 = self.coleta_valor(VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipiranga_trr1.fob_s10 = self.coleta_valor(VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipiranga_trr1.cif_s500 = self.coleta_valor(VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipiranga_trr1.fob_s500 = self.coleta_valor(VAR['id_preco_fob_s500'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços do perfil 1 realizada com sucesso")

                # Troca para o segundo perfil da TRR
                self.navegador.get(VAR['link_pedidos'])
                self.clica_botao(VAR['xpath_button_razao_social'])
                self.clica_botao(VAR['xpath_button_ipr2'])
                logger.log(f"{prefixo} - Troca para o perfil 2 realizada com sucesso")

                # Troca para o iframe e seleciona a base
                self.troca_iframe(VAR['xpath_iframe'])
                self.seleciona_opcao_menu_suspenso(VAR['xpath_select_base'], VAR['base'])
                logger.log(f"{prefixo} - Troca de iframe e base selecionada com sucesso")

                # Coleta os preços do segundo perfil da TRR
                ipiranga_trr2.cif_s10 = self.coleta_valor(VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipiranga_trr2.fob_s10 = self.coleta_valor(VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipiranga_trr2.cif_s500 = self.coleta_valor(VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipiranga_trr2.fob_s500 = self.coleta_valor(VAR['id_preco_fob_s500'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços do perfil 2 realizada com sucesso")

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
                    logger.log_error(f"\n{prefixo} - Coleta de preços da {nome_portal} não realizada!")
                    logger.log_error(f"{prefixo} - Erro: {e}")
                    break
