from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config import VAR_VBR_TRR as VAR


class ColetorVibraTRR(ColetorDePreco):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, vbr_trr:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Vibra (TRR).
        """
        tentativa = 1
        max_tentativas = 3
        nome_portal = "Vibra (TRR)"
        prefixo = "VBRTRR"
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
                logger.log(f"{prefixo} - Login realizado com sucesso")

                # Navegação para a página de pedidos e preenchimento dos campos de quantidade
                self.navegador.get(VAR['link_pedidos'])
                self.preenche_input(VAR['id_input_qtdlitros_s10'], 10000, xpath_ou_id='id')
                self.preenche_input(VAR['id_input_qtdlitros_s500'], 10000, xpath_ou_id='id')
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=5)
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=5)
                logger.log(f"{prefixo} - Navegação para a página de pedidos e preenchimento dos campos de quantidade realizados com sucesso")

                # Seleção de prazo
                self.seleciona_prazo(VAR['id_select_prazo_s10'], VAR['prazo'])
                self.seleciona_prazo(VAR['id_select_prazos500'], VAR['prazo'])
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=8)
                logger.log(f"{prefixo} - Seleção de prazo realizada com sucesso")

                # Coleta de preços FOB
                vbr_trr.fob_s10 = self.coleta_valor(VAR['xpath_preco_s10'])
                vbr_trr.fob_s500 = self.coleta_valor(VAR['xpath_preco_s500'])
                logger.log(f"{prefixo} - Coleta de preços FOB realizada com sucesso")

                # Alteração de modo
                self.muda_modo(VAR['id_select_modo_s10'], VAR['modo'])
                self.muda_modo(VAR['id_select_modo_s500'], VAR['modo'])
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=5)
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=5)
                logger.log(f"{prefixo} - Alteração de modo realizada com sucesso")

                # Coleta de preços CIF
                vbr_trr.cif_s10 = self.coleta_valor(VAR['xpath_preco_s10'])
                vbr_trr.cif_s500 = self.coleta_valor(VAR['xpath_preco_s500'])
                logger.log(f"{prefixo} - Coleta de preços CIF realizada com sucesso")

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
