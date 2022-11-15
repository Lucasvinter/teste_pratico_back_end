				teste pratico back-end 
 
1 - Baixar e Instalar o python versao 3.7.5.

2 - Abra o prompt de comando e digite: pip install pandas.

3 - Baixar e instalar o docker desktop.

4 - Baixar e intalar windows installar wsl_update_x64.

5 – Abra o power shell como administrador e digite:  docker pull mariadb.

6- Agora Digite :docker run -p 3306:3306 --name meu_banco -e MYSQL_ROOT_PASSWORD=root -d mariadb.

7- Baixar e Instalar dbeaver. 

8- Fazer a conexão como na imagem conexaodb(Password=root)
  
9 - Após conectar abre o sql editor na nova base de dados e cole o codigo abaixo para criar tabela.
  CREATE TABLE CESSAO_FUNDO (
  ID_CESSAO INT(22) NOT NULL AUTO_INCREMENT,
  ORIGINADOR VARCHAR(250) NOT NULL,
  DOC_ORIGINADOR VARCHAR(250) NOT NULL,
  CEDENTE VARCHAR(250) NOT NULL,
  DOC_CEDENTE VARCHAR(250) NOT NULL,
  CCB INT(22) NOT NULL,
  ID_EXTERNO INT(22) NOT NULL,
  CLIENTE VARCHAR(250) NOT NULL,
  CPF_CNPJ VARCHAR(50) NOT NULL,
  ENDERECO VARCHAR(250) NOT NULL,
  CEP VARCHAR(50) NOT NULL,
  CIDADE VARCHAR(250) NOT NULL,
  UF VARCHAR(50) NOT NULL,
  VALOR_DO_EMPRESTIMO DECIMAL(10,2) NOT NULL,
  VALOR_PARCELA DECIMAL(10,2) NOT NULL,
  TOTAL_PARCELAS INT(22) NOT NULL,
  PARCELA INT(22) NOT NULL,
  DATA_DE_EMISSAO DATE NOT NULL,
  DATA_DE_VENCIMENTO DATE NOT NULL,
  PRECO_DE_AQUISICAO DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (ID_CESSAO)
)

10- abra o cmd no caminho aonde se encontra o projeto e digite; python.\app.py

11- Agora e só confirmar no banco se os dados foram inseridos.
