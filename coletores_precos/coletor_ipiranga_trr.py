from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from time import time, sleep
from dotenv import load_dotenv
import os


class ColetorIpirangaTRR(ColetorDePreco):

    def __init__(self):
        super().__init__()

        load_dotenv()
        self.VAR = {
            'link': os.getenv('LINK_IPR'),
            'link_pedidos': os.getenv('LINK_PEDIDOS_IPR'),
            'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_IPR'),
            'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_IPR'),
            'login': os.getenv('LOGIN_IPR'),
            'senha': os.getenv('SENHA_IPR'),
            'xpath_button_entrar': str(os.getenv('XPATH_BUTTON_ENTRAR_IPR')),
            'xpath_button_cookies': os.getenv('XPATH_BUTTON_COOKIES_IPR'),
            'xpath_button_pedidos': os.getenv('XPATH_BUTTON_PEDIDOS_IPR'),
            'xpath_select_base': os.getenv('XPATH_SELECT_BASE_IPR'),
            'base': os.getenv('BASE_IPR'),
            'xpath_iframe': os.getenv('XPATH_IFRAME'),
            'xpath_button_razao_social': os.getenv('XPATH_BUTTON_RAZAOSOCIAL_IPR'),
            'xpath_button_ipr2': os.getenv('XPATH_BUTTON_IPR2'),
            'id_preco_cif_s10': os.getenv('ID_PRECO_CIF_S10_IPR_TRR'),
            'id_preco_fob_s10': os.getenv('ID_PRECO_FOB_S10_IPR_TRR'),
            'id_preco_cif_s500': os.getenv('ID_PRECO_CIF_S500_IPR_TRR'),
            'id_preco_fob_s500': os.getenv('ID_PRECO_FOB_S500_IPR_TRR')
        }

    def coleta_precos(self, ipiranga_trr1:Posto, ipiranga_trr2:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Ipiranga (TRR).
        """
        tentativa = 1
        max_tentativas = 3
        nome_portal = "Ipiranga TRR"
        prefixo = "IPRTRR"
        logger = Logger()

        while tentativa <= max_tentativas:
            try:
                logger.log(f"{prefixo} - Inicinando coleta de preços da {nome_portal} (tentativa {tentativa}/{max_tentativas})")
                self.navegador = self.inicializa_navegador(maximizado)
                self.inicio = time()

                # Login na página principal
                self.navegador.get(self.VAR['link'])
                self.preenche_input(self.VAR['xpath_input_login'], self.VAR['login'])
                self.preenche_input(self.VAR['xpath_input_senha'], self.VAR['senha'])
                self.clica_botao(self.VAR['xpath_button_entrar'])
                self.clica_botao(self.VAR['xpath_button_cookies'])
                self.clica_botao(self.VAR['xpath_button_pedidos'])
                logger.log(f"{prefixo} - Login e acesso a página de pedidos realizados com sucesso")

                # Troca para o iframe e seleciona a base
                self.troca_iframe(self.VAR['xpath_iframe'])
                self.seleciona_opcao_menu_suspenso(self.VAR['xpath_select_base'], self.VAR['base'])
                logger.log(f"{prefixo} - Troca de iframe e base selecionada com sucesso")

                # Coleta os preços do primeiro perfil da TRR
                ipiranga_trr1.cif_s10 = self.coleta_valor(self.VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipiranga_trr1.fob_s10 = self.coleta_valor(self.VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipiranga_trr1.cif_s500 = self.coleta_valor(self.VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipiranga_trr1.fob_s500 = self.coleta_valor(self.VAR['id_preco_fob_s500'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços do perfil 1 realizada com sucesso")

                # Troca para o segundo perfil da TRR
                self.navegador.get(self.VAR['link_pedidos'])
                self.clica_botao(self.VAR['xpath_button_razao_social'])
                self.clica_botao(self.VAR['xpath_button_ipr2'])
                logger.log(f"{prefixo} - Troca para o perfil 2 realizada com sucesso")

                # Troca para o iframe e seleciona a base
                self.troca_iframe(self.VAR['xpath_iframe'])
                self.seleciona_opcao_menu_suspenso(self.VAR['xpath_select_base'], self.VAR['base'])
                logger.log(f"{prefixo} - Troca de iframe e base selecionada com sucesso")

                # Coleta os preços do segundo perfil da TRR
                ipiranga_trr2.cif_s10 = self.coleta_valor(self.VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipiranga_trr2.fob_s10 = self.coleta_valor(self.VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipiranga_trr2.cif_s500 = self.coleta_valor(self.VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipiranga_trr2.fob_s500 = self.coleta_valor(self.VAR['id_preco_fob_s500'], xpath_ou_id='id')
                logger.log(f"{prefixo} - Coleta de preços do perfil 2 realizada com sucesso")

                self.fechar_navegador()
                self.tempo_execucao = round(time() - self.inicio, 2)
                logger.log(f"{prefixo} - Coleta de preços da {nome_portal} realizada com sucesso")
                logger.log(f"{prefixo} - Tempo de execução: {self.tempo_execucao}s")
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
                    logger.log_error(f"\n{prefixo} - Coleta de preços da {nome_portal} não realizada!")
                    logger.log_error(f"{prefixo} - Erro: {e}")
                    break
