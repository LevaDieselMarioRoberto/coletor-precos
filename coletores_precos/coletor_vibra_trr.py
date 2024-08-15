from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config.config_vbr_trr import VAR


class ColetorVibraTRR(ColetorDePreco):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, vbr_trr:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Vibra (TRR).
        """
        tentativa = 1
        max_tentativas = int(VAR['tentativas'])
        tempo_espera = int(VAR['espera_se_erro'])
        nome_portal = "Vibra (TRR)"
        prefixo = "VBRTRR"
        logger = Logger()
        telegram = Telegram()

        while tentativa <= max_tentativas:
            try:
                logger.log(f"{prefixo} - Iniciando coleta de preços da {nome_portal} (tentativa {tentativa}/{max_tentativas})")
                self.navegador = self.inicializa_navegador(maximizado, browser='edge')
                self.inicio = time()

                # Login na página principal
                self.navegador.get(VAR['link_pedidos'])
                self.preenche_input(VAR['xpath_input_login'], VAR['login'])
                self.preenche_input(VAR['xpath_input_senha'], VAR['senha'])
                self.clica_botao(VAR['xpath_button_entrar'])
                logger.log(f"{prefixo} - Login realizado")

                # Navegação para a página de pedidos e preenchimento dos campos de quantidade
                self.clica_botao(VAR['xpath_checkbox_revenda'], sleep_time=5)
                logger.log(f"{prefixo} - Selecionou 'Revenda'")
                sleep(15)

                cont = 1
                while cont <= 3:
                    try:
                        logger.log(f'{prefixo} - {cont}ª tentativa de preencher qtd de litros - s10')
                        self.preenche_input(VAR['id_input_qtdlitros_s10'], 10000, xpath_ou_id='id')
                        sleep(10)
                        break
                    except:
                        cont += 1
                        sleep(5)
                logger.log(f"{prefixo} - Preencheu quantidade de litros - s10")
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=5)
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=5)
                sleep(5)

                cont = 1
                while cont <= 3:
                    try:
                        logger.log(f'{prefixo} - {cont}ª tentativa de preencher qtd de litros - s500')
                        self.preenche_input(VAR['id_input_qtdlitros_s500'], 10000, xpath_ou_id='id')
                        sleep(10)
                        break
                    except:
                        cont += 1
                        sleep(5)
                logger.log(f"{prefixo} - Preencheu quantidade de litros - s500")
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=5)
                self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=5)

                # Seleção de prazo
                cont = 1
                while cont <= 3:
                    try:
                        logger.log(f'{prefixo} - {cont}ª tentativa de selecionar prazo (FOB)')
                        self.__altera_prazo()
                        break
                    except:
                        cont += 1
                logger.log(f"{prefixo} - Selecionou prazo para pagamento (FOB)")

                # Coleta de preços FOB
                vbr_trr.fob_s10 = self.coleta_valor(VAR['xpath_preco_s10'])
                vbr_trr.fob_s500 = self.coleta_valor(VAR['xpath_preco_s500'])
                logger.log(f"{prefixo} - Coleta de preços FOB realizada")

                # Alteração de modo
                cont = 1
                while cont <= 3:
                    try:
                        logger.log(f'{prefixo} - {cont}ª tentativa de alterar modo (CIF)')
                        sleep(5)
                        self.muda_modo(VAR['id_select_modo'], VAR['modo'], sleep_time=15)
                        break
                    except:
                        cont += 1
                logger.log(f"{prefixo} - Modo alterado para CIF")

                # Seleção de prazo
                cont = 1
                while cont <= 3:
                    try:
                        logger.log(f'{prefixo} - {cont}ª tentativa de selecionar prazo (CIF)')
                        self.__altera_prazo()
                        break
                    except:
                        cont += 1
                logger.log(f"{prefixo} - Selecionou prazo para pagamento (CIF)")

                # Coleta de preços CIF
                vbr_trr.cif_s10 = self.coleta_valor(VAR['xpath_preco_s10'])
                vbr_trr.cif_s500 = self.coleta_valor(VAR['xpath_preco_s500'])
                logger.log(f"{prefixo} - Coleta de preços CIF realizada")

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

    def __altera_prazo(self):
        sleep(8)
        self.seleciona_prazo(VAR['id_select_prazo_s10'], VAR['prazo'])
        sleep(4)
        self.seleciona_prazo(VAR['id_select_prazos500'], VAR['prazo'])
        self.clica_botao(VAR['xpath_button_atualizar'], sleep_time=8)
