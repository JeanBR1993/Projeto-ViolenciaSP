import os
import pandas as pd
from django.core.management.base import BaseCommand
from ocorrencias.models import DadosBoletim

class Command(BaseCommand):
    help = "Importa os dados de crimes de planilhas excel mineradas"

def add_arguments(self, parser):
        parser.add_argument('folder_path', type=str, help='Caminho para o diretório que contem as planixas excel')

def handle(self, *args, **kwargs):
        folder_path = kwargs['folder_path']

        # Check if the folder exists
        if not os.path.exists(folder_path):
            self.stdout.write(self.style.ERROR(f"Diretório '{folder_path}' não existe"))
            return

        # Iterate over all files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.xlsx') or filename.endswith('.xls'):
                file_path = os.path.join(folder_path, filename)
                self.stdout.write(self.style.SUCCESS(f'Processando o arquivo: {filename}'))

                # Read the Excel file
                try:
                    df = pd.read_excel(file_path, engine='openpyxl')
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erro lendo o arquivo {filename}: {e}"))
                    continue
                
                df = df.drop(df.index[0])

                # Iterate over rows and save to the model
                for index, row in df.iterrows():
                    try:
                        # Map Excel columns to model fields
                        DadosBoletim.objects.create(
                            field1=row['Column1'],  # Replace with your model fields
                            field2=row['Column2'],
                            field3=row['Column3'],
                            # Add more fields as needed
                        )
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error importing row {index + 1} in {filename}: {e}"))

                self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {filename}'))

        self.stdout.write(self.style.SUCCESS('Finished importing all files'))