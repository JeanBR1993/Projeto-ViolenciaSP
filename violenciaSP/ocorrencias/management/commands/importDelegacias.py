import pandas as pd
from django.core.management.base import BaseCommand
from ocorrencias. models import Delegacia

class Command(BaseCommand):
    help = "Extrai dados de uma planilha excel os dados de Delegacias"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Caminho do arquivo excel")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
    
        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            Delegacia.objects.create(
                nome = row["nome"],
                endereço = row["endereço"]
            )
    
        self.stdout.write(self.style.SUCCESS("Dados importados com sucesso"))