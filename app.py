import pandas as pd
import pymysql
conn = pymysql.connect(host='localhost', user='root', password='root', db='mysql', charset='utf8mb4')
cur = conn.cursor()

dados = pd.read_csv('dados.csv', header=0, sep=';', encoding='utf-8')  

for i in range(len(dados)):
    originador     = dados['Originador'          ][i]
    docOriginador  = dados['Doc Originador'      ][i]
    cedente        = dados['Cedente'             ][i]
    docCedente     = dados['Doc Cedente'         ][i]
    ccb            = dados['CCB'                 ][i]
    idExterno      = dados['Id'                  ][i]
    cliente        = dados['Cliente'             ][i]
    cpfCnpj        = dados['CPF/CNPJ'            ][i]
    endereco       = dados['Endere�o'           ][i]
    cep            = dados['CEP'                 ][i]
    cidade         = dados['Cidade'              ][i]
    uf             = dados['UF'                  ][i]
    valorEmpretimo = dados['Valor do Empr�stimo'][i].replace(',','.')
    valorParcela   = dados['Parcela R$'          ][i].replace(',','.')
    totalParcelas  = dados['Total Parcelas'      ][i]
    parcela        = dados['Parcela'             ][i]
    dataEmissao    = dados['Data de Emiss�o'    ][i]
    dataVencimento = dados['Data de Vencimento'  ][i]
    precoAquisicao = dados['Pre�o de Aquisi��o'][i]

    sql = f'INSERT INTO sys.CESSAO_FUNDO SET ORIGINADOR="{originador}", DOC_ORIGINADOR="{docOriginador}",\
         CEDENTE="{cedente}", DOC_CEDENTE="{docCedente}", CCB={ccb}, ID_EXTERNO={idExterno},CLIENTE="{cliente}",\
         CPF_CNPJ="{cpfCnpj}", ENDERECO="{endereco}", CEP="{cep}", CIDADE="{cidade}", UF="{uf}",\
         VALOR_DO_EMPRESTIMO={valorEmpretimo}, VALOR_PARCELA={valorParcela}, TOTAL_PARCELAS={totalParcelas},\
         PARCELA={parcela}, DATA_DE_EMISSAO={dataEmissao}, DATA_DE_VENCIMENTO={dataVencimento}, PRECO_DE_AQUISICAO={precoAquisicao};'

    print(sql)
    cur.execute(sql)
    print('concluido')
    conn.commit()


  



