# BMLGRAPHAPI

A biblioteca fornece funcionalidades para interagir com o SharePoint, permitindo o acesso e manipulação de planilhas, identificação de usuários e outras funcionalidades.

# Função obter_planilha()

**Descrição:** Função para retornar uma planilha do SharePoint.\
**Assinatura da função:** obter_planilha(client_id, client_secret, tenant_id, url, aba_sheet=None).\
**Retorno da função:** Dataframe (pd.read_excel()).

# Exemplo de uso: obter_planilha()

```
from main import obter_planilha

client_id = "__TOKEN__"
client_secret = "__TOKEN__"
tenant_id = "__TOKEN__"
planilha_url = "https://xyz.sharepoint.com/sites/${SITE}/${DRIVE}/NOME_DA_TABELA.xlsx"
aba_da_planilha = "__NOME DA ABA__"

planilha = obter_planilha(client_id, client_secret, tenant_id, planilha_url, aba_da_planilha)

print(planilha)
```

# Função obter_workbook()

**Descrição:** Função para retornar um workbook do SharePoint, contendo todas as sheets.\
**Assinatura da função:** obter_workbook(client_id, client_secret, tenant_id, url).\
**Retorno da função:** Workbook (load_workbook(BytesIO(content), read_only = True, data_only = True)).

# Exemplo de uso: obter_workbook()

```
import pandas as pd
from main import obter_planilha

client_id = "__TOKEN__"
client_secret = "__TOKEN__"
tenant_id = "__TOKEN__"
planilha_url = "https://xyz.sharepoint.com/sites/${SITE}/${DRIVE}/NOME_DA_TABELA.xlsx"

workbook = obter_workbook(client_id, client_secret, tenant_id, planilha_url)

aba = "__NOME DA ABA__"

print('Lendo a tabela:', aba)

linhas = workbook[aba].values
colunas = next(linhas)

planilha = pd.DataFrame(linhas, columns=colunas)

print(planilha)
```

# Função obter_id_usuario()

**Descrição:** Função para obter o id do usuário através do email.\
**Assinatura da função:** obter_id_usuario(client_id, client_secret, tenant_id, email).\
**Retorno da função:** id do usuário em formato de string.

# Exemplo de uso: obter_id_usuario()

```
from main import obter_id_usuario

client_id = "__TOKEN__"
client_secret = "__TOKEN__"
tenant_id = "__TOKEN__"
email_do_usuario = "__EMAIL DO USUARIO__"

id_usuario = obter_id_usuario(client_id, client_secret, tenant_id, email_do_usuario)

print(id_usuario)
```
