"""
Projeto Jogo Pedra-Papel-Tesoura
2024.08.13
William Jr
"""

# --> Bibliotecas
# Importa funções do arquivo modules.py
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption
from ppt import startPPT #Importa a função startPPT do arquivo ppt.py
from parimpar import startParImpar #Importa a função startParImpar do arquivo parimpar.py

# --> Constantes, Variáveis e Listas

# --> Funções

# --> Main
msgs = ['Seja Bem-vindo aos Jogos', 'PEDRA-PAPEL-TESOURA', 'PAR OU ÍMPAR'] # Mostra mensagem de inicio 
displayHeader(msgs)
msgs = ['Digite 0 --> Sair',  # Opção para o usuário não jogar nenhum dos dois jogos
        'Digite 1 --> Pedra-Papel-Tesoura', # Opção para o usuário jogar o jogo do Pedra-Papel-Tesoura
        'Digite 2 --> Par ou Ímpar'] # Opção para o usuário jogar o jogo do Par ou Impar
displayHeader(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption(opUser, ['0', '1', '2']):
  opUser = getUserOption('Sua escolha')
if(opUser == '1'): # Se o usuário quiser jogar o jogo Pedra-Papel-Tesoura
  startPPT() # Função para dar inicio ao jogo do Pedra-Papel-Tesoura
elif(opUser == '2'): # Se o usuário quiser jogar o jogo do Par ou Impar
  startParImpar() # Função para dar inicio ao jogo Par ou Impar
else: # Se o usuário não quiser jogar nenhum dos Jogos
  displayMsg('Até a Próxima...') # Aparece a mensagem ('Até a Próxima...').

  