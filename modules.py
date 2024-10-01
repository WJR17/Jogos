"""
Arquivo de Modulos
2024.08.13
William Jr
"""

# --> Bibliotecas
from random import choice # Importa a função choice da biblioteca random
from time import sleep  # Importa a função sleep  da biblioteca time

# --> Constantes, Variáveis e Listas
TAM = 50 # Tamanho da Tela
CAR = choice (['=', '*', '0', '-']) # Caracter utilizado para desenho da tela
MAR = 4 # Tamanho da Margem

# --> Funções
def clrScreen(): #Define função para limpar a tela
  print('\n'*TAM) #Mostra na tela \n == linha * TAM

def displayLine(): #Define função para mostrar uma linha de caracteres
  print(CAR*TAM) #Mostra linhas de caracteres

def displayMsg(msg): #Define função para mostrar uma msg alinhada a esquerda 
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}') #Mostra uma msg alinhada a esquerda 

def displayMsgCenter(msg): #Define função para mostrar uma msg alinhada ao Centro
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}') #Mostra uma msg alinhada ao Centro

def displayHeader(msgs): #Define função para mostrar cabeçalho
  displayLine() #Função para mostrar uma linha de caracteres
  for item in msgs:
    displayMsgCenter(item) #Se tiver item dentro da mensagem, retorna o item dentro da MsgCenter
  displayLine() #Função para mostrar uma linha de caracteres

def displayHeaderT(msgs): #Define função para mostrar cabeçalho
  displayLine() #Função para mostrar uma linha de caracteres
  for item in msgs:
    displayMsgCenter(item) #Se tiver item dentro da mensagem, retorna o item dentro da MsgCenter
    sleep(1)
  displayLine() #Função para mostrar uma linha de caracteres


def getUserOption(msg): #Define a função como resposta do usuário
  option = input(f'{CAR} {msg}: ').strip() 
  return option #Retorna a opção

def validateUserOption(option, listOptions): #Define função para mostrar se a opção escolhida pelo usuário é 'Válida' ou 'Inválida'
  if option in listOptions: #Se a opção escolhida pelo usuário estiver na lista de Opcões
    return True #Retorna True
  else: #Se a opção escolhida pelo usuário não estiver na lista de Opcões
    msgsErro = ['Opção Inválida!', 'Escolha Novamente...'] # Mostra mensagem de erro
    displayHeader(msgsErro)
    return False #Retorna False
    
# --> main

