import os
import pandas as pd
from django.core.management.base import BaseCommand
from ocorrencias.models import DadosBoletim
from pathlib import Path
import re

diretorios = [r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2021", 
              r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2022",
              r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2023",
              r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2024",
              r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2025"]


def extratorPlanilhas(path):
    # Retorna uma lista dos dados extraídos no seguinte formato:
    # (Nome da delegacia, ano dos dados, mês, natureza do crime, número de ocorrências)

    regex = re.findall(r'\\[0-9][0-9][0-9][0-9]\\', path)[0]
    ano = regex[1:5]
    print(ano)

    regex = re.findall(r'[0-9]\\.*\.xlsx', path)[0]
    local = regex[2:-5]
    print(local)

    df = pd.read_excel(path)
    df.drop(columns=["Total"], inplace=True)

    lista = []

    for index, row in df.iterrows():
        lista.append((local, ano, "Janeiro", row["Natureza"], row["Janeiro"]))
        lista.append((local, ano, "Fevereiro", row["Natureza"], row["Fevereiro"]))
        lista.append((local, ano, "Marco", row["Natureza"], row["Marco"]))
        lista.append((local, ano, "Abril", row["Natureza"], row["Abril"]))
        lista.append((local, ano, "Maio", row["Natureza"], row["Maio"]))
        lista.append((local, ano, "Junho", row["Natureza"], row["Junho"]))
        lista.append((local, ano, "Julho", row["Natureza"], row["Julho"]))
        lista.append((local, ano, "Agosto", row["Natureza"], row["Agosto"]))
        lista.append((local, ano, "Setembro", row["Natureza"], row["Setembro"]))
        lista.append((local, ano, "Outubro", row["Natureza"], row["Outubro"]))
        lista.append((local, ano, "Novembro", row["Natureza"], row["Novembro"]))
        lista.append((local, ano, "Dezembro", row["Natureza"], row["Dezembro"]))
    
    return lista



class Command(BaseCommand):
    help = "Importa os dados de crimes de planilhas excel mineradas"

    def handle(self, *args, **kwargs):
        
        diretorios = [r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2021", 
              r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2022",
              r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2023",
              r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2024",
              r"C:\Users\Administrator\Desktop\Projeto ViolenciaSP\violenciaSP\dadosNCrimes\2025"]
        
        for path in paths:
            self.stdout.write(self.style.SUCCESS(f'Scanning directory: {path}'))

            if not os.path.exists(path):
                self.stdout.write(self.style.ERROR(f'Path does not exist: {path}'))
                continue

            if not os.path.isdir(path):
                self.stdout.write(self.style.ERROR(f'Not a directory: {path}'))
                continue