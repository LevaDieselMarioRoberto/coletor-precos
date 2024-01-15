from coletores_precos.coletor_preco import ColetorDePreco
from posto import Posto
from time import time, sleep
from dotenv import load_dotenv
import os


class ColetorIpirangaPostos(ColetorDePreco):

    def __init__(self):
        super().__init__()

        load_dotenv()
        self.VAR = {
            'link': os.getenv('LINK_IPR'),
            'login': os.getenv('LOGIN_IPR_POSTOS'),
            'senha': os.getenv('SENHA_IPR_POSTOS'),
            'xpath_input_login': os.getenv('XPATH_INPUT_LOGIN_IPR'),
            'xpath_input_senha': os.getenv('XPATH_INPUT_SENHA_IPR'),
            'xpath_button_entrar': os.getenv('XPATH_BUTTON_ENTRAR_IPR'),
            'xpath_button_cookies': os.getenv('XPATH_BUTTON_COOKIES_IPR'),
            'link_pedidos': os.getenv('LINK_PEDIDOS_IPR'),
            'xpath_button_razaosocial': os.getenv('XPATH_BUTTON_RAZAOSOCIAL_IPR'),
            'xpath_iframe': os.getenv('XPATH_IFRAME'),
            'id_preco_cif_etanol': os.getenv('ID_PRECO_CIF_ETANOL_IPR'),
            'id_preco_fob_etanol': os.getenv('ID_PRECO_FOB_ETANOL_IPR'),
            'id_preco_cif_gasolina': os.getenv('ID_PRECO_CIF_GASOLINA_IPR'),
            'id_preco_fob_gasolina': os.getenv('ID_PRECO_FOB_GASOLINA_IPR'),
            'id_preco_cif_gasolinaadt': os.getenv('ID_PRECO_CIF_GASOLINAADT_IPR'),
            'id_preco_fob_gasolinaadt': os.getenv('ID_PRECO_FOB_GASOLINAADT_IPR'),
            'id_preco_cif_s10': os.getenv('ID_PRECO_CIF_S10_IPR'),
            'id_preco_fob_s10': os.getenv('ID_PRECO_FOB_S10_IPR'),
            'id_preco_cif_s500': os.getenv('ID_PRECO_CIF_S500_IPR'),
            'id_preco_fob_s500': os.getenv('ID_PRECO_FOB_S500_IPR'),
            'xpath_button_distrito': os.getenv('XPATH_BUTTON_DISTRITO_IPR'),
            'xpath_button_itirapua': os.getenv('XPATH_BUTTON_ITIRAPUA_IPR'),
            'xpath_button_ppp': os.getenv('XPATH_BUTTON_PPP_IPR'),
            'xpath_button_pitstop': os.getenv('XPATH_BUTTON_PITSTOP_IPR')
        }

    def coleta_precos(self, ipr_gasstation:Posto, ipr_distrito:Posto, ipr_itirapua:Posto, ipr_ppp:Posto, ipr_pitstop:Posto, maximizado=False):
        """
        Coleta preços de s10 e s500 aditivados do portal da Ipiranga (Postos).
        """
        tentativa = 1
        max_tentativas = 3
        nome_portal = "Ipiranga Postos"
        prefixo = "IPRPST"

        while tentativa <= max_tentativas:
            try:
                self.log(f"{prefixo} - Inicinando coleta de preços da {nome_portal} (tentativa {tentativa}/{max_tentativas})")
                self.navegador = self.inicializa_navegador(maximizado)
                self.inicio = time()

                # Login na página principal
                self.navegador.get(self.VAR['link'])
                self.preenche_input(self.VAR['xpath_input_login'], self.VAR['login'])
                self.preenche_input(self.VAR['xpath_input_senha'], self.VAR['senha'])
                self.clica_botao(self.VAR['xpath_button_entrar'])
                self.clica_botao(self.VAR['xpath_button_cookies'])
                self.log(f"{prefixo} - Login realizado com sucesso")

                self.seleciona_filial()                                     # Gás Station
                ipr_gasstation.cif_etanol = self.coleta_valor( self.VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_gasstation.fob_etanol = self.coleta_valor( self.VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_gasstation.cif_gasolina = self.coleta_valor( self.VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_gasstation.fob_gasolina = self.coleta_valor( self.VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_gasstation.cif_gasolina_ad = self.coleta_valor( self.VAR['id_preco_cif_gasolinaadt'], xpath_ou_id='id')
                ipr_gasstation.fob_gasolina_ad = self.coleta_valor( self.VAR['id_preco_fob_gasolinaadt'], xpath_ou_id='id')
                ipr_gasstation.cif_s10 = self.coleta_valor( self.VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_gasstation.fob_s10 = self.coleta_valor( self.VAR['id_preco_fob_s10'], xpath_ou_id='id')
                self.log(f"{prefixo} - Coleta de preços do Gás Station realizada com sucesso")

                self.seleciona_filial(self.VAR['xpath_button_distrito'])    # Distrito
                ipr_distrito.cif_etanol = self.coleta_valor(self.VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_distrito.fob_etanol = self.coleta_valor(self.VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_distrito.cif_gasolina = self.coleta_valor(self.VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_distrito.fob_gasolina = self.coleta_valor(self.VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_distrito.cif_s10 = self.coleta_valor(self.VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_distrito.fob_s10 = self.coleta_valor(self.VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipr_distrito.cif_s500 = self.coleta_valor(self.VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipr_distrito.fob_s500 = self.coleta_valor(self.VAR['id_preco_fob_s500'], xpath_ou_id='id')
                self.log(f"{prefixo} - Coleta de preços do Distrito realizada com sucesso")

                self.seleciona_filial(self.VAR['xpath_button_itirapua'])    # Itirapuã
                ipr_itirapua.cif_etanol = self.coleta_valor(self.VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_itirapua.fob_etanol = self.coleta_valor(self.VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_itirapua.cif_gasolina = self.coleta_valor(self.VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_itirapua.fob_gasolina = self.coleta_valor(self.VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_itirapua.cif_s10 = self.coleta_valor(self.VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_itirapua.fob_s10 = self.coleta_valor(self.VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipr_itirapua.cif_s500 = self.coleta_valor(self.VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipr_itirapua.fob_s500 = self.coleta_valor(self.VAR['id_preco_fob_s500'], xpath_ou_id='id')
                self.log(f"{prefixo} - Coleta de preços de Itirapuã realizada com sucesso")

                self.seleciona_filial(self.VAR['xpath_button_ppp'])         # PPP
                ipr_ppp.cif_etanol = self.coleta_valor(self.VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_ppp.fob_etanol = self.coleta_valor(self.VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_ppp.cif_gasolina = self.coleta_valor(self.VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_ppp.fob_gasolina = self.coleta_valor(self.VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_ppp.cif_s10 = self.coleta_valor(self.VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_ppp.fob_s10 = self.coleta_valor(self.VAR['id_preco_fob_s10'], xpath_ou_id='id')
                self.log(f"{prefixo} - Coleta de preços do PPP realizada com sucesso")

                self.seleciona_filial(self.VAR['xpath_button_pitstop'])     # Pit Stop
                ipr_pitstop.cif_etanol = self.coleta_valor(self.VAR['id_preco_cif_etanol'], xpath_ou_id='id')
                ipr_pitstop.fob_etanol = self.coleta_valor(self.VAR['id_preco_fob_etanol'], xpath_ou_id='id')
                ipr_pitstop.cif_gasolina = self.coleta_valor(self.VAR['id_preco_cif_gasolina'], xpath_ou_id='id')
                ipr_pitstop.fob_gasolina = self.coleta_valor(self.VAR['id_preco_fob_gasolina'], xpath_ou_id='id')
                ipr_pitstop.cif_gasolina_ad = self.coleta_valor(self.VAR['id_preco_cif_gasolinaadt'], xpath_ou_id='id')
                ipr_pitstop.fob_gasolina_ad = self.coleta_valor(self.VAR['id_preco_fob_gasolinaadt'], xpath_ou_id='id')
                ipr_pitstop.cif_s10 = self.coleta_valor(self.VAR['id_preco_cif_s10'], xpath_ou_id='id')
                ipr_pitstop.fob_s10 = self.coleta_valor(self.VAR['id_preco_fob_s10'], xpath_ou_id='id')
                ipr_pitstop.cif_s500 = self.coleta_valor(self.VAR['id_preco_cif_s500'], xpath_ou_id='id')
                ipr_pitstop.fob_s500 = self.coleta_valor(self.VAR['id_preco_fob_s500'], xpath_ou_id='id')
                self.log(f"{prefixo} - Coleta de preços do Pit Stop realizada com sucesso")

                self.fechar_navegador()
                self.tempo_execucao = round(time() - self.inicio, 2)
                self.log(f"{prefixo} - Coleta de preços da {nome_portal} realizada com sucesso")
                self.log(f"{prefixo} - Tempo de execução: {self.tempo_execucao}s")
                break

            except:
                tentativa += 1
                self.fechar_navegador()

                if tentativa <= max_tentativas:
                    self.log_error(f"{prefixo} - Erro na coleta de preços da {nome_portal}")
                    self.log_error(f"{prefixo} - Nova tentativa de coleta em 30 segundos...")
                    sleep(30)
                    continue
                else:
                    self.log_error(f"\n{prefixo} - Coleta de preços da {nome_portal} não realizada!")
                    break

    def seleciona_filial(self, filial=''):
        """
        Seleciona uma filial (posto) específica no menu suspenso.
        """
        self.navegador.get(self.VAR['link_pedidos'])
        sleep(3)

        if str(filial) != '':
            self.clica_botao(self.VAR['xpath_button_razaosocial'])
            self.clica_botao(filial)
            self.navegador.get(self.VAR['link_pedidos'])
            sleep(2)

        self.troca_iframe(self.VAR['xpath_iframe'])
