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
