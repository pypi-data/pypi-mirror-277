# BMLGRAPHAPI

Pacote para obter tabelas xlsx do SharePoint através de seu link.

# Função obter_planilha()

Assinatura da função: obter_planilha(client_id, client_secret, tenant_id, planilha_url, aba_sheet=None).
Retorno da função: Dataframe (pd.read_excel()).

# Exemplo de uso
```
import pandas as pd
from main import obter_planilha

client_id = "__TOKEN__"
client_secret = "__TOKEN__"
tenant_id = "__TOKEN__"
planilha_url = "https://xyz.sharepoint.com/sites/${SITE}/${DRIVE}/NOME_DA_TABELA.xlsx"
aba_da_planilha = "__NOME DA ABA__"

planilha = obter_planilha(client_id, client_secret, tenant_id, planilha_url, aba_da_planilha)

print(planilha)
```