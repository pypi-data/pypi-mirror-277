# GraphAPI e requests
from msal import *
import requests

# Excel
from openpyxl import load_workbook
from io import BytesIO

# Decodicação da URL
from urllib.parse import unquote 

# Pandas
import pandas as pd

# Credenciais de acesso
ACCESS_TOKEN = ""

def obter_access_token(client_id, client_secret, tenant_id):
  resource_id =  "https://graph.microsoft.com/"
  scopes = [resource_id + '.default']
    
  authority = f"https://login.microsoftonline.com/{tenant_id}"

  app = ConfidentialClientApplication(
    client_id, authority=authority, client_credential=client_secret
  )

  token = app.acquire_token_for_client(scopes=scopes)
  return token["access_token"]

    
# Função para acessar os metadados de um site SharePoint e retornar seu ID
def obter_id_site(nome_site):
  url = f"https://graph.microsoft.com/v1.0/sites?search={nome_site}"
  
  headers = {
      "Authorization": f"Bearer {ACCESS_TOKEN}",
      "Content-Type": "application/json"
  }
  
  response = requests.get(url, headers=headers)
  data = response.json()
  
  return data["value"][0]["id"]

# Função para acessar os metadados de um drive SharePoint e retornar seu ID
def obter_id_drive(site_id):
  url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
  
  headers = {
      "Authorization": f"Bearer {ACCESS_TOKEN}",
      "Content-Type": "application/json"
  }
  
  response = requests.get(url, headers=headers)
  data = response.json()

  return data["value"][0]["id"]

# Função para retornar os metadados de um arquivo ou pasta SharePoint localizado no root do drive
def obter_metadados_item_root(site_id, drive_id, nome_item):
  url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root:/{nome_item}"
  
  headers = {
      "Authorization": f"Bearer {ACCESS_TOKEN}",
      "Content-Type": "application/json"
  }
  
  response = requests.get(url, headers=headers)
  data = response.json()

  return data

# Função para retornar os metadados de um arquivo ou pasta SharePoint
def obter_metadados_item(site_id, drive_id, pasta_id, nome_item):
  url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/{pasta_id}/children"
  
  headers = {
      "Authorization": f"Bearer {ACCESS_TOKEN}",
      "Content-Type": "application/json"
  }
  
  response = requests.get(url, headers=headers)
  data = response.json()

  for arq in data["value"]:
    if(arq["name"] == nome_item):
      return arq

# Função para retornar uma planilha através do link
def obter_conteudo_planilha(arquivo_info, aba_sheet=None):
  # Link do download do arquivo
  download_url = arquivo_info['@microsoft.graph.downloadUrl']

  if aba_sheet==None:
    planilha = pd.read_excel(download_url)
  else:
    planilha = pd.read_excel(download_url, sheet_name=aba_sheet)

  return planilha

# Função para retornar um workbook através do link
def obter_conteudo_workbook(arquivo_info):
  # Link do download do arquivo
  download_url = arquivo_info['@microsoft.graph.downloadUrl']

  # Conexão com a planilha
  response = requests.get(download_url)
  content = response.content

  workbook = load_workbook(BytesIO(content), read_only = True, data_only = True)
  
  return workbook

# Função para retornar o conteúdo de uma planilha localizada no root do drive
def arquivo_no_root(nome_site, nome_arquivo, aba_sheet=None, tipo_retorno="planilha"):
  site_id = obter_id_site(nome_site)

  drive_id = obter_id_drive(site_id)

  arquivo_info = obter_metadados_item_root(site_id, drive_id, nome_arquivo)

  if tipo_retorno == "planilha":
    return obter_conteudo_planilha(arquivo_info, aba_sheet)
  else:
    return obter_conteudo_workbook(arquivo_info)

# Função para retornar o conteúdo de uma planilha localizada diretamente em uma pasta root do drive
def arquivo_em_pasta_root(info_url, aba_sheet=None, tipo_retorno="planilha"):
  nome_site = info_url[0]
  nome_pasta_root = info_url[2]
  nome_arquivo = info_url[3]

  site_id = obter_id_site(nome_site)

  drive_id = obter_id_drive(site_id)

  pasta_id = obter_metadados_item_root(site_id, drive_id, nome_pasta_root)["id"]

  arquivo_info = obter_metadados_item(site_id, drive_id, pasta_id, nome_arquivo)

  if tipo_retorno == "planilha":
    return obter_conteudo_planilha(arquivo_info, aba_sheet)
  else:
    return obter_conteudo_workbook(arquivo_info)

# Função para retornar o conteúdo de uma planilha localizada dentro de multiplas pastas
def arquivo_em_pastas(info_url, aba_sheet=None, tipo_retorno="planilha"):
  arquivo_index = len(info_url) - 1

  nome_site = info_url[0]
  nome_pasta_root = info_url[2]

  pastas = info_url[3:arquivo_index]

  nome_arquivo = info_url[arquivo_index]

  site_id = obter_id_site(nome_site)

  drive_id = obter_id_drive(site_id)

  pasta_id = obter_metadados_item_root(site_id, drive_id, nome_pasta_root)["id"]

  for pasta in pastas:
    pasta_id = obter_metadados_item(site_id, drive_id, pasta_id, pasta)["id"]

  arquivo_info = obter_metadados_item(site_id, drive_id, pasta_id, nome_arquivo)

  if tipo_retorno == "planilha":
    return obter_conteudo_planilha(arquivo_info, aba_sheet)
  else:
    return obter_conteudo_workbook(arquivo_info)

# Função para retornar uma planilha ou workbook no SharePoint
def obter_planilha(client_id, client_secret, tenant_id, url, aba_sheet=None):
  global ACCESS_TOKEN
  ACCESS_TOKEN = obter_access_token(client_id, client_secret, tenant_id)

  info_url = unquote(url).split("/")

  del info_url[0:4]
  
  tipo_retorno = "planilha"

  if(len(info_url) == 3):
    return arquivo_no_root(info_url[0], info_url[2], aba_sheet, tipo_retorno)
  elif(len(info_url) == 4):
    return arquivo_em_pasta_root(info_url, aba_sheet, tipo_retorno)
  else:
    return arquivo_em_pastas(info_url, aba_sheet, tipo_retorno)

# Função para retornar um workbook no SharePoint
def obter_workbook(client_id, client_secret, tenant_id, url):
  global ACCESS_TOKEN
  ACCESS_TOKEN = obter_access_token(client_id, client_secret, tenant_id)

  info_url = unquote(url).split("/")

  del info_url[0:4]
  
  tipo_retorno = "workbook"
  aba_sheet = None

  if(len(info_url) == 3):
    return arquivo_no_root(info_url[0], info_url[2], aba_sheet, tipo_retorno)
  elif(len(info_url) == 4):
    return arquivo_em_pasta_root(info_url, aba_sheet, tipo_retorno)
  else:
    return arquivo_em_pastas(info_url, aba_sheet, tipo_retorno)
  
# Função para obter o id do usuário através do email
def obter_id_usuario(client_id, client_secret, tenant_id, email):
  ACCESS_TOKEN = obter_access_token(client_id, client_secret, tenant_id)
  
  graph_url = f"https://graph.microsoft.com/v1.0/users?$filter=mail eq '{email}'"

  headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
             'Content-Type': 'application/json'}
  
  response = requests.get(graph_url, headers=headers)
  
  return response.json().get('value')[0]['id']
  