from coletores_precos.coletor_preco import ColetorDePreco
from posto import Posto
from time import time, sleep
from dotenv import load_dotenv
import os


class ColetorRaizenTRR(ColetorDePreco):

    def __init__(self):
        super().__init__()

        load_dotenv()
        self.VAR = {
            'link': os.getenv('LINK_RZN'),
            'login': os.getenv('LOGIN_RZN'),
            'senha': os.getenv('SENHA_RZN'),
            'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_RZN'),
            'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_RZN'),
            'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_RZN'),
            'link_precos': os.getenv('LINK_PRECOS_RZN'),
            'xpath_preco_fob_s10': os.getenv('XPATH_PRECO_FOB_S10_RZN'),
            'xpath_preco_fob_s500': os.getenv('XPATH_PRECO_FOB_S500_RZN'),
            'xpath_preco_cif_s10': os.getenv('XPATH_PRECO_CIF_S10_RZN'),
            'xpath_preco_cif_s500': os.getenv('XPATH_PRECO_CIF_S500_RZN')
        }
        

    def coleta_precos(self, raizen_trr:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Raizen (TRR).
        """
        tentativa = 1
        max_tentativas = 3
        nome_portal = "Raízen TRR"
        prefixo = "RZNTRR"

        while tentativa <= max_tentativas:
            try:
                print(f"{prefixo} - Inicinando coleta de preços da {nome_portal} (tentativa {tentativa}/{max_tentativas})")
                self.navegador = self.inicializa_navegador(maximizado)
                self.inicio = time()

                # Login na página principal
                self.navegador.get(self.VAR['link'])
                self.preenche_input(self.VAR['xpath_input_login'], self.VAR['login'])
                self.preenche_input(self.VAR['xpath_input_senha'], self.VAR['senha'])
                self.clica_botao(self.VAR['xpath_button_entrar'])
                sleep(3)
                self.navegador.get(self.VAR['link_precos'])     # Acessa a página de preços
                print(f"{prefixo} - Login e acesso a página de pedidos realizados com sucesso")
                sleep(10)

                # Coleta os preços
                raizen_trr.cif_s10 = self.coleta_valor(self.VAR['xpath_preco_cif_s10'])
                raizen_trr.fob_s10 = self.coleta_valor(self.VAR['xpath_preco_fob_s10'])
                raizen_trr.cif_s500 = self.coleta_valor(self.VAR['xpath_preco_cif_s500'])
                raizen_trr.fob_s500 = self.coleta_valor(self.VAR['xpath_preco_fob_s500'])

                self.fechar_navegador()
                self.tempo_execucao = round(time() - self.inicio, 2)
                print(f"{prefixo} - Coleta de preços da {nome_portal} realizada com sucesso")
                print(f"{prefixo} - Tempo de execução: {self.tempo_execucao}s")
                break

            except:
                tentativa += 1
                self.fechar_navegador()

                if tentativa <= max_tentativas:
                    print(f"{prefixo} - Erro na coleta de preços da {nome_portal}")
                    print(f"{prefixo} - Nova tentativa de coleta em 30 segundos...")
                    sleep(30)
                    continue
                else:
                    print(f"\n{prefixo} - Coleta de preços da {nome_portal} não realizada!")
                    break
