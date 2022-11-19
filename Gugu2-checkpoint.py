#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Instalando biblioteca pymysql
get_ipython().system('pip install pymysql')


# In[11]:


get_ipython().system('pip install mysql-connector-python')


# In[12]:


#Importando bibliotecas usadas
import os
import pymysql
import pyodbc
import pandas as pd
import mysql.connector


# In[13]:


#Configurando conexão
host = os.getenv('127.0.0.1')
port = os.getenv('3306')
user = os.getenv('root')
password = os.getenv('')
database = os.getenv('fintech')

conn = pymysql.connect(
    host=host,
    port=int(3306),
    user="root",
    passwd=password,
    db= 'fintech',
    charset='utf8mb4')

cursor = conn.cursor()


# In[14]:


#Verificando primeiros 10 registros da tabela usada
df = pd.read_sql_query("SELECT * FROM conta", conn)
df.tail(10)


# In[15]:


#Bloco principal do código
def main():
    x = menu()
    if x == 1:
        print("--------Método--------")
        opcao1()
    else:
        if sair() != 0:
            if x is None or x == '':
                print("Opção inválida")
                main()


# In[16]:


#Bloco para finalizar a aplicação, quando o usuário digitar 0 (ZERO)
def sair():
    x = input("Se deseja sair, digite 0: ")
    if not x is None or not x == '':x = int(x)
    if x == 0:
        print("Final")
    return x


# In[17]:


#Bloco que configura e imprime o menu
def menu():
    print("Bem vindo ao seu registro financeiro: ")
    print("1. Definir método de pagamento")
    print("0. Sair")
    opcao = input("Digite a opção desejada: ")
    if not opcao is None or not opcao == '':inte = int(opcao)
    return inte


# In[18]:


#Bloco com formas de pagamento
def opcao1():
    print("Temos essas formas de pagamento:\n" + "1. Dinheiro\n" + "2. Débito\n" + "3. Crédito\n" + "4. Ticket")
    x = input("Opção desejada: ")
    if not x is None or not x == '':x = int(x)
    if x == 1:
        print("--------Dinheiro--------")
        valorGasto("Dinheiro")
    elif x == 2:
        print("--------Débito--------")
        valorGasto("Débito")
    elif x == 3:
        print("--------Crédito--------")
        valorGasto("Crédito")
    elif x == 4:
        print("--------Ticket--------")
        valorGasto("Ticket")
    else:
        if sair() != 0:
            if x is None or x == '':
                print("--------Opção inválida--------")
                opcao1()


# In[19]:


#Especificando o tipo de Conta Fixa
def subtipo_cf(metodo, tipo, valor):
    print("Sub-Tipo de Conta Fixa:\n" + "1. Internet\n" + "2. Telefone\n" + "3. Casa (aluguel, condomínio, reformas)\n")
    x = input("Opção desejada: ")
    if not x is None or not x == '':x = int(x)
    if x == 1:
        print("Inserindo em Conta Fixa - Internet")
        subtipo = "Internet"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 2:
        print("Inserindo em Conta Fixa - Telefone")
        subtipo = "Telefone"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 3:
        print("Inserindo em Conta Fixa - Telefone")
        subtipo = "Casa"
        insercFeita(metodo, tipo, subtipo, valor)
    else:
        if sair() != 0:
            if x is None or x == '':
                print("Sub-Tipo inválido!! Selecione novamente entre os sub-tipos exibidos.")
                subtipo_cd(metodo, tipo, valor)


# In[20]:


#Especificando o tipo de Compras Diversas
def subtipo_cd(metodo, tipo, valor):
    print("Tipo de Compra Diversa:\n" + "1. PETs\n" + "2. Farmácia\n" + "3. Vícios\n" + "4. Amigos\n" + "5. Aleatória\n")
    x = input("Opção desejada: ")
    if not x is None or not x == '':x = int(x)
    if x == 1:
        print("Inserindo em Compra Diversa - PETs")
        subtipo = "PETs"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 2:
        print("Inserindo em Compra Diversa - Farmácia")
        subtipo = "Farmácia"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 3:
        print("Inserindo em Compra Diversa - Vícios")
        subtipo = "Vícios"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 4:
        print("Inserindo em Compra Diversa - Amigos")
        subtipo = "Amigos"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 5:
        print("Inserindo em Compra Diversa - Aleatória")
        subtipo = "Aleatória"
        insercFeita(metodo, tipo, subtipo, valor)
    else:
        if sair() != 0:
            if x is None or x == '':
                print("Sub-Tipo inválido!! Selecione novamente entre os sub-tipos exibidos.")
                subtipo_cd(metodo, tipo, valor)


# In[21]:


#Especificando o tipo de Compras Essenciais
def subtipo_ce(metodo, tipo, valor):
    print("Sub-Tipo de Compra Essencial:\n" + "1. Alimentação\n" + "2. Roupas\n" + "3. Beleza\n" + "4. Saúde\n")
    x = input("Opção desejada: ")
    if not x is None or not x == '':x = int(x)
    if x == 1:
        print("Inserindo em Compra Essencial - Alimentação")
        subtipo = "Alimentação"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 2:
        print("Inserindo em Compra Essencial - Roupas")
        subtipo = "Roupas"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 3:
        print("Inserindo em Compra Essencial - Beleza")
        subtipo = "Beleza"
        insercFeita(metodo, tipo, subtipo, valor)
    if x == 4:
        print("Inserindo em Compra Essencial - Saúde")
        subtipo = "Saúde"
        insercFeita(metodo, tipo, subtipo, valor)
    else:
        if sair() != 0:
            if x is None or x == '':
                print("Sub-Tipo inválido!! Selecione novamente entre os sub-tipos exibidos.")
                subtipo_cd(metodo, tipo, valor)


# In[22]:


#Inserindo um registro na tabela
def insTable (metodo, tipo, subtipo, valor):
    comentario = input("DIgite um comentário: ")
    args = (metodo, tipo, subtipo, valor, comentario)
    query = cursor.execute("INSERT INTO fintech.conta (metodo, tipo, subtipo, valor, coment, dat) VALUES (%s, %s, %s, %s, %s, sysdate())", (args))
    query = cursor.execute("COMMIT")


# In[23]:


#Realizando o SELECT na tabela
def selec():
    selec = pd.read_sql("SELECT metodo, tipo, subtipo, valor, coment, DATE_FORMAT(dat,'%d/%m/%Y') AS Data_PTBR FROM fintech.conta", conn)
    print(selec)


# In[24]:


#Confirmando se a inserção foi feita e qual foi feita
def insercFeita(metodo, tipo, subtipo, valor):
    print("Registrado em ", tipo, " - ", subtipo)
    insTable(metodo, tipo, subtipo, valor)
    selec()


# In[25]:


#Definindo as categorias dos registros
def categoria(metodo, valor):
    print("Categorias\n" + "1. Contas fixas\n" + "2. Compras diversas\n" + "3. Compras essenciais\n")
    categoria = input("Selecione a categoria: ")
    if not categoria is None or not categoria == '':categoria = int(categoria)
    if categoria == 1:
        tipo = "Contas Fixas" 
        subtipo_cf(metodo, tipo, valor)
    elif categoria == 2:
        tipo = "Contas Diversas" 
        subtipo_cd(metodo, tipo, valor)
    elif categoria == 3:
        tipo = "Contas Essenciais" 
        subtipo_ce(metodo, tipo, valor)
    else:
        if sair() != 0:
            if x is None or x == '':
                print("Categoria inválida!")
                categoria(metodo, valor) 


# In[26]:


#Solicita o valor gasto e em qual categoria foi feito
def valorGasto(metodo):
    valor = float(input("Valor gasto: "))
    print("Em qual categoria foi gasto: ")
    categoria(metodo, valor)


# In[27]:


main()


# In[ ]:




