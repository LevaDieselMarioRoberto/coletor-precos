from telegram import Telegram
from config import BASE_DIR
import json

class Posto():

    def __init__(self, nome):
        self.nome = nome
        self.cif_etanol = None
        self.fob_etanol = None
        self.cif_gasolina_ad = None
        self.fob_gasolina_ad = None
        self.cif_gasolina = None
        self.fob_gasolina = None
        self.cif_s10 = None
        self.fob_s10 = None
        self.cif_s500 = None
        self.fob_s500 = None
        self.precos_cif = [self.cif_etanol, self.cif_gasolina_ad, self.cif_gasolina, self.cif_s10, self.cif_s500]
        self.precos_fob = [self.fob_etanol, self.fob_gasolina_ad, self.fob_gasolina, self.fob_s10, self.fob_s500]

    def imprime_precos(self):
        print(f"\nPreços {self.nome}:")
        print("                CIF           FOB")

        if self.cif_etanol and self.fob_etanol != None:  
            print(f"Etanol         {self.cif_etanol}       {self.fob_etanol}")

        if self.cif_gasolina_ad and self.fob_gasolina_ad != None:
            print(f"Gas Ad         {self.cif_gasolina_ad}       {self.fob_gasolina_ad}")

        if self.cif_gasolina and self.fob_gasolina != None:
            print(f"Gas C          {self.cif_gasolina}       {self.fob_gasolina}")

        if self.cif_s10 and self.fob_s10 != None:
            print(f"s10            {self.cif_s10}       {self.fob_s10}")

        if self.cif_s500 and self.fob_s500 != None:
            print(f"s500           {self.cif_s500}       {self.fob_s500}")

    def compara_precos(self):

        precos_atuais = {       # Cria um dicionário com os preços atuais
            "CIF Etanol": self.cif_etanol,
            "FOB Etanol": self.fob_etanol,
            "CIF Gasolina Ad": self.cif_gasolina_ad,
            "FOB Gasolina Ad": self.fob_gasolina_ad,
            "CIF Gasolina": self.cif_gasolina,
            "FOB Gasolina": self.fob_gasolina,
            "CIF S10": self.cif_s10,
            "FOB S10": self.fob_s10,
            "CIF S500": self.cif_s500,
            "FOB S500": self.fob_s500
        }

        arquivo_json = BASE_DIR + f"precos/{self.nome}.json"

        try:    # Tenta abrir o arquivo JSON existente
            with open(arquivo_json, 'r') as f:
                precos_anteriores = json.load(f)
        except FileNotFoundError:
            precos_anteriores = {}

        mensagem = None

        # Compara os preços atuais com os preços anteriores
        for chave, valor_atual in precos_atuais.items():
            valor_anterior = precos_anteriores.get(chave)

            if valor_anterior is not None and valor_atual is not None:
                if valor_atual != valor_anterior:

                    if mensagem is None: mensagem = f"❗ Alteração em {self.nome}:\n"

                    mensagem += f"\n{chave}: {valor_anterior} ➡️ {valor_atual}"

                    if valor_atual > valor_anterior: mensagem += " ⤴️ ❌"
                    else: mensagem += " ⤵️ ✅"

        if mensagem is not None:
            telegram = Telegram()
            telegram.enviar_mensagem(mensagem)

            # Salva os preços atuais no arquivo JSON
            with open(arquivo_json, 'w') as f:
                json.dump(precos_atuais, f, indent=2)
