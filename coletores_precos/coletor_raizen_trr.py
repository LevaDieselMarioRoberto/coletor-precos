from coletores_precos.coletor_preco import ColetorDePreco
from logger import Logger
from posto import Posto
from telegram import Telegram
from time import time, sleep
from config import VAR_RZN_TRR as VAR


class ColetorRaizenTRR(ColetorDePreco):

    def __init__(self):
        super().__init__()

    def coleta_precos(self, raizen_trr:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Raizen (TRR).
        """
        tentativa = 1
        max_tentativas = 3
        nome_portal = "Raízen (TRR)"
        prefixo = "RZNTRR"
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
