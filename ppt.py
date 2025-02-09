"""
Jogo do Pedra-Papel-Tesoura
2024.08.13
William Jr
"""

# Bibliotecas
from modules import clrScreen, displayHeader, validateUserOption, getUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT # Importa funções do arquivo modules.py
from random import randint # Importa a função randint da biblioteca random
from time import sleep  # Importa a função sleep  da biblioteca time

# Constantes, Variáveis e Listas
msgsInicio = ['Seja bem vind@ aoJogo do PEDRA-PAPEL-TESOURA,',
  'desenvolvido por: William Jr',
  'BOA SORTE!']
msgs = []
playAgain = ''
playerScore = 0
computerScore = 0

# Funções
def startPPT(): # define a função para dar inicio ao jogo Pedra-Papel-Tesoura
  while(True):
    clrScreen() #Função para limpar a tela
    displayHeader(msgsInicio) 
    # função para começar o jogo
    playPPT 
    playAgain = getUserOption('Deseja jogar novamente[s/n]')    
    while not validateUserOption(playAgain, ['s', 'n','S', 'N']):
      playAgain = getUserOption('Deseja jogar novamente[s/n]')
    if playAgain.lower() != 's':
      break

def displayMenu():
  msgs = ['Escolha:',
    '[0] --> Pedra',
    '[1] --> Papel',
    '[2] --> Tesoura']
  displayLine()
  for msg in msgs:
    displayMsg(msg)
  displayLine()



def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs.append(typeScore)
  msgs.append (f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)
 

def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'Empate!'
  elif (playerChoice == '0' and computerChoice == '2') or \
        (playerChoice == '1' and computerChoice == '0') or \
        (playerChoice == '2' and computerChoice == '1'):
    play = f"{playerChoiceStr} vence {computerChoiceStr}"
    result = 'Você Ganhou!'
  else:
    play = f"{computerChoiceStr} vence {playerChoiceStr}"
    result = 'Você Perdeu!'
  msgs = ['Jogada do Player: ' + playerChoiceStr,
          'Jogado do PC: ' + computerChoiceStr,
          play, result]
  displayHeaderT(msgs)
  return result

def playPPT():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore <2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0','1','2']):
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice, computerChoice)
    if "Ganhou" in result:
      playerScore += 1
    elif "Perdeu" in result:
      computerScore += 1
    if playerScore< 2 and computerScore < 2:
      displayScore("PLACAR", playerScore, computerScore)
    sleep(1)
  displayScore("PLACAR FINAL",  playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['Parabéns','YOU WIN!'])
  else:
     displayHeader(['Parabéns','YOU LOUSE!'])
  
# Main
