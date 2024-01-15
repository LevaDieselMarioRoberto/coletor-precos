from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from dotenv import load_dotenv
import os


class ColetorVibraJanjao(ColetorDePreco):

    def __init__(self):
        super().__init__()

        load_dotenv(self.env)
        self.VAR = {
            'link': os.getenv('LINK_VBR'),
            'login': os.getenv('LOGIN_VBR_JANJAO'),
            'senha': os.getenv('SENHA_VBR_JANJAO'),
            'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_VBR'),
            'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_VBR'),
            'link_pedidos': os.getenv('LINK_PEDIDOS_VBR'),
            'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_VBR'),
            'xpath_button_atualizar': os.getenv('XPATH_BUTTON_ATUALIZAR_VBR'),
            'xpath_preco_etanol': os.getenv('XPATH_PRECO_ETANOL_VBRJJ'),
            'xpath_preco_gasolina': os.getenv('XPATH_PRECO_GASOLINA_VBRJJ'),
            'xpath_preco_s10': os.getenv('XPATH_PRECO_S10_VBRJJ'),
            'xpath_preco_s500': os.getenv('XPATH_PRECO_S500_VBRJJ'),
            'modo': os.getenv('MODO_VBR'),
            'id_select_modo_etanol': os.getenv('ID_SELECT_MODO_ETANOL_VBRJJ'),
            'id_select_modo_gasolina': os.getenv('ID_SELECT_MODO_GASOLINA_VBRJJ'),
            'id_select_modo_s10': os.getenv('ID_SELECT_MODO_S10_VBRJJ'),
            'id_select_modo_s500': os.getenv('ID_SELECT_MODO_S500_VBRJJ')
        }

    def coleta_precos(self, vbr_jj:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Vibra (Janjão).
        """
        tentativa = 1
        max_tentativas = 3
        nome_portal = "Vibra (Janjão)"
        prefixo = "VBRJJ"
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
                logger.log(f"{prefixo} - Login realizado com sucesso")

                # Navegação para a página de pedidos
                self.navegador.get(self.VAR['link_pedidos'])
                logger.log(f"{prefixo} - Navegação para a página de pedidos realizada com sucesso")

                # Coleta de preços FOB
                vbr_jj.fob_etanol = self.coleta_valor(self.VAR['xpath_preco_etanol'])
                vbr_jj.fob_gasolina = self.coleta_valor(self.VAR['xpath_preco_gasolina'])
                vbr_jj.fob_s10 = self.coleta_valor(self.VAR['xpath_preco_s10'])
                vbr_jj.fob_s500 = self.coleta_valor(self.VAR['xpath_preco_s500'])
                logger.log(f"{prefixo} - Coleta de preços FOB realizada com sucesso")

                # Alteração de modo
                self.muda_modo(self.VAR['id_select_modo_etanol'], self.VAR['modo'], sleep_time=10)
                self.muda_modo(self.VAR['id_select_modo_gasolina'], self.VAR['modo'], sleep_time=10)
                self.muda_modo(self.VAR['id_select_modo_s10'], self.VAR['modo'], sleep_time=10)
                self.muda_modo(self.VAR['id_select_modo_s500'], self.VAR['modo'], sleep_time=10)
                self.clica_botao(self.VAR['xpath_button_atualizar'], sleep_time=5)
                self.clica_botao(self.VAR['xpath_button_atualizar'], sleep_time=5)
                logger.log(f"{prefixo} - Alteração de modo realizada com sucesso")

                # Coleta de preços CIF
                vbr_jj.cif_etanol = self.coleta_valor(self.VAR['xpath_preco_etanol'])
                vbr_jj.cif_gasolina = self.coleta_valor(self.VAR['xpath_preco_gasolina'])
                vbr_jj.cif_s10 = self.coleta_valor(self.VAR['xpath_preco_s10'])
                vbr_jj.cif_s500 = self.coleta_valor(self.VAR['xpath_preco_s500'])
                logger.log(f"{prefixo} - Coleta de preços CIF realizada com sucesso")

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
                    telegram = Telegram()
                    telegram.enviar_mensagem(f"Erro na coleta de preços da {nome_portal} 😕")
                    logger.log_error(f"\n{prefixo} - Coleta de preços da {nome_portal} não realizada!")
                    logger.log_error(f"{prefixo} - Erro: {e}")
                    break
