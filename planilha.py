import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from posto import Posto
from logger import Logger
from datetime import datetime
from config import PLANILHA_DIR


class Planilha():

    def __init__(self):
        self.df = pd.DataFrame()
        self.arquivo = PLANILHA_DIR
        self.logger = Logger()

    def cria_df_precos(self, lista_postos:Posto):
        cont = 1
        dados = {"TIPO": ["Etanol", "Gas Ad", "Gas C", "S10", "S500"]}
        for posto in lista_postos:
            dados[f"CIF{cont}"] = [posto.cif_etanol, posto.cif_gasolina_ad, posto.cif_gasolina, posto.cif_s10, posto.cif_s500]
            dados[f"FOB{cont}"] = [posto.fob_etanol, posto.fob_gasolina_ad, posto.fob_gasolina, posto.fob_s10, posto.fob_s500]
            cont += 1
        self.df = pd.DataFrame(dados)

    def salva_planilha(self, lista_postos:Posto):
        self.cria_df_precos(lista_postos)

        try:
            writer = pd.ExcelWriter(self.arquivo, engine='openpyxl', datetime_format='dd/mm/yyyy HH:MM:SS', date_format='dd/mm/yyyy', mode='a', if_sheet_exists='replace')
        except FileNotFoundError:
            writer = pd.ExcelWriter(self.arquivo, engine='openpyxl', datetime_format='dd/mm/yyyy HH:MM:SS', date_format='dd/mm/yyyy', mode='w')
        except PermissionError:
            self.logger.log("Feche o arquivo excel!")
            num = 1
            self.arquivo = self.arquivo.replace("resultados_precos", f"resultados_precos({num})")
            while True:
                try:
                    writer = pd.ExcelWriter(self.arquivo, engine='openpyxl', datetime_format='dd/mm/yyyy HH:MM:SS', date_format='dd/mm/yyyy', mode='w')
                    break
                except:
                    self.arquivo = self.arquivo.replace(f"resultados_precos({num})", f"resultados_precos({num+1})")
                    num += 1
                    continue

        self.df.to_excel(writer, sheet_name='Precos', index=False)
        writer.close()
        self.logger.log(f"Resultados salvos em: {self.arquivo}")
        self.formata_planilha()

    def formata_planilha(self):
        workbook = load_workbook(self.arquivo)
        sheet = workbook['Precos']
        sheet.insert_rows(1)

        amarelo, verde, roxo = "FFFFCC", "D8E4BC", "E4DFEC"
        cores = [amarelo, amarelo, amarelo, amarelo, amarelo, verde, amarelo, amarelo, verde, roxo]
        titulos = ['Pitstop', 'Distrito', 'Gas Station', 'Itirapuã', 'PPP', 'Janjão', 'TRR Ipiranga1', 'TRR Ipiranga2', 'TRR Vibra', 'TRR Raízen']
        centralizado = Alignment(horizontal='center', vertical='center')
        bordas = Border(
            left=Side(border_style="thin", color="000000"),
            right=Side(border_style="thin", color="000000"),
            top=Side(border_style="thin", color="000000"),
            bottom=Side(border_style="thin", color="000000"),
        )

        for coluna, titulo, cor in zip(range(2, 22, 2), titulos, cores):
            sheet.merge_cells(start_row=1, start_column=coluna, end_row=1, end_column=coluna + 1)
            sheet.cell(row=1, column=coluna, value=titulo)
            sheet.cell(row=1, column=coluna).font = Font(bold=True)
            sheet.cell(row=1, column=coluna).fill = PatternFill(start_color=cor, end_color=cor, fill_type="solid")
            sheet.cell(row=1, column=coluna).alignment = centralizado
            sheet.cell(row=1, column=coluna).border = bordas

        sheet.cell(row=1, column=21).border = bordas

        data_e_hora = datetime.now().strftime("%d/%m-%H:%M")
        sheet.cell(row=1, column=1).value = data_e_hora
        sheet.cell(row=1, column=1).alignment = centralizado
        sheet.cell(row=1, column=1).font = Font(size=8)

        workbook.save(self.arquivo)
        self.logger.log("Planilha formatada com sucesso!")
