import os
from getpass import getuser
from dotenv import load_dotenv

user = getuser()

BASE_DIR = f"C:/Users/{user}/Documents/Projetos/coletor_precos/"

PLANILHA_DIR = f"C:/Users/{user}/OneDrive - MARIO ROBERTO TRANSP REVENDEDORA D OLEO DIESEL/Leva Diesel/Logística/resultados_precos.xlsx"

ARQUIVO_LOG = BASE_DIR + "dist/coletor.log"
ARQUIVO_ENV = BASE_DIR + ".env" # Necessário ser explícito para execução de tarefa automática do Windows

load_dotenv(ARQUIVO_ENV)

CONTROLS = {
    'COLETA_HABILITADA': os.getenv('COLETA_HABILITADA', 'true').lower() == 'true',
    'COLETAR_IPR_TRR': os.getenv('COLETAR_IPR_TRR', 'true').lower() == 'true',
    'COLETAR_VBR_TRR': os.getenv('COLETAR_VBR_TRR', 'true').lower() == 'true',
    'COLETAR_RZN_TRR': os.getenv('COLETAR_RZN_TRR', 'true').lower() == 'true',
    'COLETAR_VBR_JJ': os.getenv('COLETAR_VBR_JJ', 'true').lower() == 'true',
    'COLETAR_IPR_POSTOS': os.getenv('COLETAR_IPR_POSTOS', 'true').lower() == 'true',
    'MAXIMIZADO_IPR_TRR': os.getenv('MAXIMIZADO_IPR_TRR', 'false').lower() == 'true',
    'MAXIMIZADO_VBR_TRR': os.getenv('MAXIMIZADO_VBR_TRR', 'false').lower() == 'true',
    'MAXIMIZADO_RZN_TRR': os.getenv('MAXIMIZADO_RZN_TRR', 'false').lower() == 'true',
    'MAXIMIZADO_VBR_JJ': os.getenv('MAXIMIZADO_VBR_JJ', 'false').lower() == 'true',
    'MAXIMIZADO_IPR_POSTOS': os.getenv('MAXIMIZADO_IPR_POSTOS', 'false').lower() == 'true',
    'IMPRIME_PRECOS_TERMINAL': os.getenv('IMPRIME_PRECOS_TERMINAL', 'false').lower() == 'true',
    'SALVA_PRECOS_PLANILHA': os.getenv('SALVA_PRECOS_PLANILHA', 'false').lower() == 'true',
    'ENVIA_PRECOS_TELEGRAM': os.getenv('ENVIA_PRECOS_TELEGRAM', 'false').lower() == 'true',
}

TELEGRAM_CONFIG = {
    'TOKEN': os.getenv('TOKEN'),
    'IDCHAT': os.getenv('IDCHAT'),
}
