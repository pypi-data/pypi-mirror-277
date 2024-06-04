from random import randint
from time import sleep
#models
from models.card import Card
from models.bot import Bot
#schemas
from schemas.type_card import TypeCardInit, TypeCardGet
from schemas.card import CardInit
from schemas.bot import BotInit
#functions
from functions.deck import get_deck, get_cards, calculate_win, calculate_envido
from functions.sistem import print_slow, cls

class Game():
    def __init__(self, center= 29, time = 1, objective = 30) -> None:
        self.time = time
        self.objective = objective
        self.bot:Bot = None
        self.start_pc = True
        self.play_pc = self.start_pc
        self.quiero_pc = None
        self.center = center
        self.score:list[int] = [0,0] #0:gamer, 1:computer
        self.actual_score:list[int] = [0,0]
        self.envido = 1 #0:ya jugado, 1:nada, 2:envido, 3:real envido, 4:falta envido 
        self.truco = 1               #1:nada, 2:truco,  3:retruco,     4:vale cuatro
        self.cards_played = {
            1: [],
            2: [],
            3: []
        }
        cards = get_cards()
        self.cards:list[list[Card]] = [
            cards[0:3], cards[3:7] 
        ]
        self.truco_options = {
            1: 'Normal',
            2: 'Truco',
            3: 'Retruco',
            4: 'Vale Cuatro'
        }
        self.envido_options = {
            2: 'Envido',
            3: 'Real Envido',
            4: 'Falta Envido'
        }
        


    def start(self):
        cls()
        self.bot = Bot(BotInit(name='fercho'))
        if randint(0,1) == 0:
            self.start_pc = False
        else:
            self.start_pc = True
        print(self.bot)
        self.score = [0,0]
        #cls()
        print('Empieza la partida de truco')
        self.print_score()
        self.start_round()

    def start_round(self):
        self.actual_score:list[int] = [0,0] #0:gamer, 1:computer
        self.score_envido:int = 0
        self.envido:int = 1 #0:ya jugado, 1:nada, 2:envido, 3:real envido, 4: falta envido 
        self.truco:int = 1  #0:,          1:nada, 2:truco,  3:retruco,     4:vale cuatro
        self.end_round:bool = False
        self.cards_played = {
            'pc': [],
            'player': []
        }
        cards = get_cards()
        self.cards:list[list[Card]] = [
            cards[0:3], cards[3:7] 
        ]
        self.all_cards = self.cards
        self.cards_envido = [
            calculate_envido(self.cards[0]),
            calculate_envido(self.cards[1]),
        ]
        self.envido_option_points = {
            2: 2,
            3: 3,
            4: 0
        }

        self.play_pc = self.start_pc
        self.win_pc = None
        while not self.end_round:
            round = min(len(self.cards_played['pc']),len(self.cards_played['player']))+1
            
            cls()
            print(f'ROUND: {round} - BOT: {self.bot}')
            self.print_played_cards()
            

            if len(self.cards_played['pc']) == len(self.cards_played['player']) and round!=1:
                if self.cards_played['pc'][-1].value < self.cards_played['player'][-1].value:
                    self.play_pc = True
                elif self.cards_played['pc'][-1].value > self.cards_played['player'][-1].value:
                    self.play_pc = False
                    
            if self.play_pc:
                print('cartas disponibles'.center( self.center))
                self.print_card(cards = self.cards[0]) 
                sleep(self.time)
                card_pc,envido,truco = self.bot.play_round(round=round,cards=self.cards[1],cards_played=self.cards_played,envido=self.envido,truco=self.truco,quiero_pc=self.quiero_pc)
                if card_pc:
                    self.cards_played['pc'].append(card_pc)
                    self.cards[1].remove(card_pc)
                    self.play_pc = not self.play_pc
                elif envido:
                    sleep(self.time)
                    self.respond_envido(envido)
                elif truco:
                    sleep(self.time)
                    self.respond_truco(bot_call=True)
                    sleep(self.time*2.5)
            else:
                sleep(self.time)
                self.play_player()
            
            response = self.check_round(round)
            
            
        cls()
        self.print_played_cards()
        print_slow(response.upper())
        sleep(self.time)
        cls()
        print(f'winner:{self.win_pc}, truco:{self.truco}')
        if self.win_pc is False:
            self.actual_score[0] += self.truco
        elif self.win_pc is True:
            self.actual_score[1] += self.truco
        self.print_score()

    def play_player(self, only_cards = False):
        player_cards = self.cards[0]
        valid_inputs = []
        
        print('cartas disponibles'.center( self.center))
        self.print_card(cards = player_cards) 
        
        if only_cards==False:
            txt = ''
            for i in range(len(player_cards)):
                txt+= f'{i+1}: {player_cards[i]}  '
                valid_inputs.append(str(i+1))
            print_slow(txt)
            valid_calls = self.options_call()
            value = self.input_value(valid_inputs=valid_inputs+valid_calls)
            
            if value in ['1','2','3']:
                card_choice = player_cards[int(value)-1]
                self.cards_played['player'].append(card_choice)
                self.cards[0].remove(card_choice)
                self.play_pc = not self.play_pc
                
            elif value == 'M':
                self.mazo_call()
            elif value == 'E':
                valid_inputs = self.envido_call(refuse=True)
                value = self.input_value(valid_inputs=valid_inputs)
                if value in ['1','2','3']:
                    value = int(value)+1
                    print_slow(f'Jugador: {self.envido_options[value]}')  
                    sleep(self.time) 
                    responses_bot = self.bot.respond_envido(self.all_cards[1],at_least=value)
                    if responses_bot == 0:
                        print_slow(f'{self.bot}: No quiero...')
                        self.actual_score[0] = max(self.score_envido,1)
                        self.envido = 0
                    elif responses_bot == value:
                        print_slow(f'{self.bot}: Quiero...')
                        self.envido = value
                        self.score_envido += self.envido_option_points[value]
                        self.calculate_envido()
                    else:
                        self.score_envido += self.envido_option_points[value]
                        self.respond_envido(responses_bot)
                    sleep(self.time*2.5) 

            elif value == 'T' and self.truco!=4:
                    print_slow(f'Le canto {self.truco_options[self.truco+1]} amigo')
                    responses_bot = self.bot.respond_truco(self.cards[1],self.cards_played,self.truco)
                    sleep(self.time)
                    if responses_bot == True:
                        self.truco += 1
                        self.respond_truco()
                    elif responses_bot == False:
                        self.truco += 1
                        self.quiero_pc = True
                        print_slow(f'{self.bot.name}: Quiero')       
                    else:
                        self.win_pc = False
                        self.end_round = True
                        print_slow(f'{self.bot.name}: NO QUIERO NADA')
                    sleep(self.time*2.5)

    def respond_envido(self, envido):
        print_slow(f'{self.bot.name}: {self.envido_options[envido]}')
        valid_inputs = self.envido_call(refuse=False,at_least=envido+1)
        value = self.input_value(valid_inputs=valid_inputs)
        
        if value == 'N':
            print_slow(f'Jugador: No quiero...')
            self.actual_score[1] = max(self.score_envido,1)
            self.envido = 0
        elif value == 'Q':
            print_slow(f'Jugador: Quiero...')
            self.score_envido += self.envido_option_points[envido]
            self.envido = envido
            self.calculate_envido()
        else:
            self.envido = envido
            value = int(value)+1
            print_slow(f'Jugador: {self.envido_options[value]}')  
            sleep(self.time) 
            responses_bot = self.bot.respond_envido(self.all_cards[1],at_least=value)
            if responses_bot == 0:
                print_slow(f'{self.bot}: No quiero...')
                self.actual_score[0] = max(self.score_envido,1)
                self.envido = 0
            elif responses_bot == value:
                print_slow(f'{self.bot}: Quiero...')
                self.envido = value
                self.score_envido += self.envido_option_points[value]
                self.calculate_envido()
            else:
                self.score_envido += self.envido_option_points[responses_bot]
                self.respond_envido(responses_bot)
            sleep(self.time*2.5) 

    def calculate_envido(self):
        sleep(self.time)
        cls()
        print()
        print('Envido:'.center( self.center))
        print('--------------------'.center( self.center))
        print(f'{self.bot.name}'.center( self.center))
        #print_slow(f'{self.cards_envido[1]}'.center( self.center))
        print()
        print('--------------------'.center( self.center))
        print(f'vs'.center( self.center))
        #print(f'{self.cards_envido[0]}'.center( self.center))
        print()
        print('--------------------'.center( self.center))
        print()
        sleep(self.time*2)
        cls()
        print()
        print('Envido:'.center( self.center))
        print('--------------------'.center( self.center))
        print(f'{self.bot.name}'.center( self.center))
        print(f'{self.cards_envido[1]}'.center( self.center))
        print('--------------------'.center( self.center))
        print(f'vs'.center( self.center))
        #print(f'{self.cards_envido[0]}'.center( self.center))
        print()
        print('--------------------'.center( self.center))
        print()
        sleep(self.time*1.5)
        cls()
        print()
        print('Envido:'.center( self.center))
        print('--------------------'.center( self.center))
        print(f'{self.bot.name}'.center( self.center))
        print(f'{self.cards_envido[1]}'.center( self.center))
        print('--------------------'.center( self.center))
        print(f'vs'.center( self.center))
        print(f'{self.cards_envido[0]}'.center( self.center))
        print('--------------------'.center( self.center))
        print()
        sleep(self.time*1.5)

        if self.cards_envido[0] > self.cards_envido[1] or (self.cards_envido[0] == self.cards_envido[1] and self.start_pc == False) :
            if self.envido == 4:
                self.score_envido = self.objective-self.score[1]
            self.actual_score[0] = self.score_envido
            print_slow(f'Ganaste {self.score_envido} punto{"s" if self.score_envido!=1 else ""}!!')
        else:
            if self.envido == 4:
                self.score_envido = self.objective-self.score[0]
            self.actual_score[1] = self.score_envido
            print_slow(f'Perdiste... {self.score_envido} punto{"s" if self.score_envido!=1 else ""}... :(')
        self.envido = 0
        sleep(self.time*2.5)

    def respond_truco(self, bot_call = False):
        if bot_call:
            self.truco += 1
            print_slow(f'{self.bot.name}: {self.truco_options[self.truco].capitalize()}!!!')
        else:
            try:
                print_slow(f'{self.bot.name}: {self.truco_options[self.truco+1].upper()}!!')
                self.truco += 1
            except:
                print_slow(f'{self.bot.name}: {self.truco_options[self.truco].upper()}!!')
            
        sleep(self.time*1.5)
        valid_inputs = self.truco_call(refuse=False)
        value = self.input_value(valid_inputs=valid_inputs)
        if value == 'Q':
            self.quiero_pc = False
            print_slow('Player: Quiero >:)')
            
        elif value == 'N':
            self.truco += -1
            self.mazo_call(txt='Player: No quiero...')
        if value == 'T':
            
            print_slow(f'Player: Le canto {self.truco_options[self.truco+1]} amigo')
            responses_bot = self.bot.respond_truco(self.cards[1],self.cards_played,self.truco+1)
            sleep(self.time)
            if responses_bot == True:
                self.truco += 1
                self.respond_truco()
            elif responses_bot == False:
                self.truco += 1
                self.quiero_pc = True
                print_slow(f'{self.bot.name}: Quiero')
            else:
                self.win_pc = False
                self.end_round = True
                print_slow(f'{self.bot.name}: NO QUIERO NADA')
            
                  

    #Options calls
    def options_call(self):
        txt = ''
        valid_inputs = []
        if self.envido not in [0,4]:
            if self.cards_played['player']:
                self.envido = 0
            else:
                txt += 'E: Envido, '
                valid_inputs.append('E')
        
        if self.truco != 4 and self.quiero_pc is not True:
            txt += f'T: {self.truco_options[self.truco+1].capitalize()}, '
            valid_inputs.append('T')

        txt += 'M: Mazo'
        valid_inputs.append('M')
        print_slow(txt)
        return valid_inputs
    
    def envido_call(self,at_least=1, refuse = False):
        txt = ''
        valid_inputs = []
        if at_least<=4:
            for i in self.envido_options:
                if i>=at_least:
                    txt += f'{i-1}: {self.envido_options[i]}, '
                    valid_inputs.append(str(i-1))
        if refuse:
            txt += f'V: volver'
            valid_inputs.append('V')
        else:
            txt += f'Q: Quiero, N: No Quiero'
            valid_inputs.append('Q')
            valid_inputs.append('N')
        print_slow(txt)
        return valid_inputs

    def truco_call(self,at_least=1, refuse = False):
        txt = ''
        valid_inputs = []
        if self.truco != 4:
            valid_inputs.append('T')
            txt = f'T: {self.truco_options[self.truco+1].capitalize()}, '
        if refuse:
            txt += f'V: volver'
            valid_inputs.append('V')
        else:
            txt += f'Q: Quiero, N: No Quiero'
            valid_inputs.append('Q')
            valid_inputs.append('N')
        print_slow(txt)
        return valid_inputs


    def mazo_call(self,txt = 'Player se ha ido al mazo'):
        self.end_round = True
        self.win_pc = True
        print_slow(txt) #MAZOWORD
        sleep(self.time)
    

    #responses
    

    def check_round(self,round):
        win_rounds,none = calculate_win(self.cards_played)
        response = ''
        winner = None
        player_text = f'has ganado la ronda!'
        pc_text = f'{self.bot.name} gano la rona...'
        if win_rounds['pc'] == win_rounds['player'] == win_rounds['draw'] == 1:
            if self.cards_played['pc'][0].value > self.cards_played['player'][0].value:
                winner = 1
            else:
                winner = 0
            self.end_round = True
        elif win_rounds['pc'] == 2 or (win_rounds['pc'] == win_rounds['draw'] == 1 and round != 3):
            winner = 1
            self.end_round = True
        elif win_rounds['player'] == 2 or (win_rounds['player'] == win_rounds['draw'] == 1 and round != 3):
            winner = 0
            self.end_round = True
        elif win_rounds['player'] == win_rounds['draw'] == 1 and round == 3:
            i=0
            if self.cards_played['pc'][0].value == self.cards_played['player'][0].value:
                i=1
                if self.cards_played['pc'][1].value == self.cards_played['player'][1].value:
                    i=2
            if self.cards_played['pc'][i].value > self.cards_played['player'][i].value:
                winner = 1
                self.end_round = True
            elif self.cards_played['pc'][i].value < self.cards_played['player'][i].value:
                winner = 0
                self.end_round = True
            elif self.start_pc:
                winner = 1
                self.end_round = True
            else:
                winner = 0
                self.end_round = True
        if winner == 0:
            self.win_pc = False
            response = player_text
        elif winner == 1:
            self.win_pc = True
            response = pc_text  
        return response


    #input functions
    def input_value(self, valid_inputs = ['M']):
        while True:
            try:
                value:str = input('>> ')
                if value.upper() in valid_inputs:
                    return value.upper()
            except:
                pass
            print(f'(Ayuda) Elige una de estas opciones {valid_inputs}. Opcion elegida: {value}')

    #print functions
    def print_score(self,aument_score=True):
        self.score[0] += self.actual_score[0]
        self.score[1] += self.actual_score[1]
        txt = (len(self.bot.name)-2)*' '+'vs'
        
        print('#'* self.center)
        print(f'{txt} - {self.bot.name}'.center(self.center))
        print(f'{self.score[0]:02d} - {self.score[1]:02d}'.center(self.center))
        print('#'* self.center)
        sleep(self.time)

    def print_card(self, cards = [], card = None):
        if card:
            print('o-------o')
            print(f'|{card.number:02d}  {card.type_card.emoji} |')
            print(f'|  {card.type_card.abbrevation}  |')
            print(f'|{card.type_card.emoji}   {card.number:02d}|')
            print('o-------o')
        else: 
            frame = 'o-------o '* len(cards)
            top = ''
            middle = ''
            bottom = ''
            for i in range(len(cards)):
                top += f'|{cards[i].number:02d}   {cards[i].type_card.emoji}| '
                middle += f'|  {cards[i].type_card.abbrevation}  | '
                bottom += f'|{cards[i].type_card.emoji}   {cards[i].number:02d}| '
            print(frame)
            print(top)
            print(middle)
            print(bottom)
            print(frame)

    def print_played_cards(self):
        print(f'Cartas Jugadas'.center( self.center))
        print(f'{self.bot.name}'.center( self.center))
        print('--------------------'.center( self.center))
        self.print_card(cards=self.cards_played['pc'])
        print('vs'.center( self.center))
        print('--------------------'.center( self.center))
        self.print_card(cards=self.cards_played['player'])
        print('--------------------'.center( self.center))