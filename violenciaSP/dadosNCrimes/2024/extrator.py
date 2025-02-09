import requests as re

pagina = re.get("https://www.ssp.sp.gov.br/estatistica/dados-mensais")

print(pagina.text)