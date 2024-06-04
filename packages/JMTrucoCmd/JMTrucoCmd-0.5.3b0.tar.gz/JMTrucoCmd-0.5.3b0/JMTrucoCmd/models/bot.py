from random import randint
#models
from models.stats import Stats
#schemas
from schemas.bot import BotInit
from schemas.stats import StatsInit
#functions
from functions.deck import calculate_envido,calculate_truco, calculate_win, get_deck

class Bot():
    def __init__(self,bot_init:BotInit) -> None:
        self.name:str = (bot_init.name or 'Pc').capitalize()
        self.stats:Stats = Stats(
            StatsInit(
                aggressive=bot_init.aggressive or randint(1,10),
                liar=bot_init.liar or randint(1,10),
                fisherman=bot_init.fisherman or randint(1,10),
                score_truco=bot_init.score_truco or randint(8,9),
                score_envido=bot_init.score_envido or randint(21,27)
            )
        )
    def __str__(self) -> str:
        return f'nombre: {self.name}, stats: ({self.stats})'
    
    def play_round(self,round:int=None,cards:list=[],cards_played:list=[],envido=1,truco = 1,quiero_pc = True):
        if (round not in [1,2,3]):
            round = 1
        
        if round == 1:
            if envido==1:
                return None, 2, None
                call_envido = self.probabily_call_envido(cards)
                if call_envido is not 0:
                    return None, call_envido, None
                    pass
        if truco!=4 and quiero_pc is not False:
            call_truco = self.probabily_call_truco(cards,cards_played,truco,round)
            if call_truco is not False:
                return None, None, call_truco
                pass
        
        card = self.pick_card(cards,cards_played,round)
        return card,None,None            

                    
    def probabily_call_envido(self,cards):
        #0:ya jugado, 1:nada, 2:envido, 3:real envido, 4: falta envido 
        actual_points_envido = calculate_envido(cards)
        if actual_points_envido>=self.stats.score_envido: #tiene puntos
            #probabilidad de ir a la pesca
            if(randint(0,80) <= randint(0,self.stats.fisherman*10-self.stats.aggressive)):
                return False
            #probabilidad de que cantar
            n = 10-randint(1, self.stats.aggressive)
            if actual_points_envido >= self.stats.score_envido+n:
                if randint(0,2) <= 1:
                    return 4
            if actual_points_envido >= self.stats.score_envido+n//2:
                if randint(0,2) <= 1:
                    return 3
            return 2
        #no tiene puntos
        if randint(0,self.stats.liar*10) >= randint(0,100):
            n = randint(1, (self.stats.aggressive+self.stats.liar)//2)
            if n>=5:
                return 4
            if n>=3:
                return 3
            return 2
        return 0

    def probabily_call_truco(self,cards,cards_played,truco,round):
        #self.truco = 1  #0:,          1:nada, 2:truco,  3:retruco,     4:vale cuatro
        actual_points_truco = calculate_truco(cards)
        win_rounds, card_to_responses = calculate_win(cards_played)
        extra = 0
        if win_rounds['player'] > win_rounds['pc']:
            extra = -3
        elif win_rounds['player'] < win_rounds['pc']:
            extra = 2
        
        
        if not card_to_responses:
            pass
        else:
            for card in cards:
                if card.value>card_to_responses.value:
                    if card_to_responses.value<self.stats.score_truco+1:
                        extra+=1
        n = (extra+self.stats.score_truco)*len(cards) + randint(-2,2)

        if win_rounds['draw'] <= 1:
            if card_to_responses:
                for card in cards:
                    if card.value<card_to_responses.value:
                        return truco+1
                        
        good_carts = actual_points_truco< n
        aggresive = randint(0,100-len(cards)*20) <= randint(0,10+(self.stats.aggressive*10)) 
        liar = randint(0,80) <= randint(0,self.stats.liar*10)
        #print(f'cartas: {actual_points_truco} < expectativas: {self.stats.score_truco*len(cards)} or {n} ')
        #print(f'aggresive:{aggresive}, good carts:{good_carts}, liar: {liar}')
        
        if good_carts:      #tiene buenas cartas
            if(aggresive):
                return truco+1
        else:               #no tiene buenas cartas
            if(liar):
                return truco+1
        return False
    
    def pick_card(self,cards,cards_played,round):
        win_rounds, card_to_responses = calculate_win(cards_played)
        cards_sorted_value = self.value_card(cards)
        n = randint(1,100)
        aggresive = randint(0,80) <= randint(0,self.stats.aggressive*10)
        if win_rounds['draw']:
            return cards_sorted_value[0]
        elif win_rounds['pc'] > win_rounds['player']:
            return cards_sorted_value[-1]
        elif win_rounds['pc'] < win_rounds['player']:
            if not card_to_responses:
                if n<=self.stats.aggressive//2+self.stats.liar+5:
                    return cards_sorted_value[1]
                else:
                    return cards_sorted_value[0]
            else:
                min = self.min_winner_value_card(cards_sorted_value,card_to_responses.value)
                if min:
                    return min
        if round == 1:
            if not card_to_responses:
                if aggresive:
                    if n<=5:
                        return cards_sorted_value[0]
                    else:
                        return cards_sorted_value[1]
                if n<50:
                    return cards_sorted_value[1]
                return cards_sorted_value[2]
            else:
                if n<=self.stats.liar+5:
                    return cards_sorted_value[-1]
                min = self.min_winner_value_card(cards_sorted_value,card_to_responses.value)
                if min:
                    return min
        return cards_sorted_value[0]
    
    def value_card(self,cards):
        cards_sorted = sorted(cards, key=lambda card: card.value)
        return cards_sorted

    def min_winner_value_card(self,cards, value):
        min = None
        for i in cards:
            if value>i.value:
                if not min:
                    min = i
                if min.value < i.value:
                    min = i
        return min
    
    def respond_envido(self,cards,at_least=2):
        #0:ya jugado, 1:nada, 2:envido, 3:real envido, 4: falta envido 
        actual_points_envido = calculate_envido(cards)
        if actual_points_envido>=self.stats.score_envido+at_least+randint(-1,1): #tiene puntos
            #probabilidad de que cantar
            n = 10-randint(1, self.stats.aggressive)
            if actual_points_envido >= self.stats.score_envido+n:
                if randint(0,2) <= 1:
                    return max(at_least,4)
            if actual_points_envido >= self.stats.score_envido+n//2:
                if randint(0,2) <= 1:
                    return max(at_least,3)
            return max(at_least,2)
        #no tiene puntos
        if randint(0,self.stats.liar*10) >= randint(0,100) and at_least!=4:

            liar = randint(1, (self.stats.aggressive+self.stats.liar)//2)
            if liar>=5:
                return max(4,at_least)
            if liar>=3:
                return max(3,at_least)
            return max(2,at_least)
        return 0

    def respond_truco(self,cards,cards_played,truco):
        #self.truco = 1  #0:,          1:nada, 2:truco,  3:retruco,     4:vale cuatro
        actual_points_truco = calculate_truco(cards)
        win_rounds, card_to_responses = calculate_win(cards_played)

        extra = -truco
        if win_rounds['player'] > win_rounds['pc']:
            extra = -3
        elif win_rounds['player'] < win_rounds['pc']:
            extra = 2
        elif win_rounds['draw'] !=0:
            extra = -1
        
        
        if not card_to_responses:
            n = (extra+self.stats.score_truco)*(len(cards)+1) + randint(0,self.stats.aggressive//2)
            if len(cards_played['pc']) > len(cards_played['player']):
                actual_points_truco+=cards_played['pc'][-1].value
                if cards_played['pc'][-1].value < self.stats.score_truco:
                    n = (extra+self.stats.score_truco)*(len(cards)+1) + randint(0,self.stats.aggressive)
        else:
            n = (extra+self.stats.score_truco)*len(cards) + randint(0,self.stats.aggressive//2)
            can_defeated = False
            for card in cards:
                if card.value>card_to_responses.value:
                    n+=2
                else:
                    n+=-1
                    can_defeated = True
            if not can_defeated and (win_rounds['player'] == 1 or win_rounds['draw'] == 1):
                if card_to_responses.value == 1:
                    return None
                n = 0
        
        good_carts = actual_points_truco<= n 
        aggresive = randint(0,80) <= randint(0,10+(self.stats.aggressive*10)+len(cards)*10) 
        liar = randint(0,80) <= randint(0,self.stats.liar*10)
        #print(f'cartas: {actual_points_truco} < expectativas: {self.stats.score_truco*len(cards)} or {n} ')
        #print(f'aggresive:{aggresive}, good carts:{good_carts}, liar: {liar}')
        if good_carts:      #tiene buenas cartas
            if(aggresive) and truco!=4:
                return True
            return False
        else:               #no tiene buenas cartas
            if(liar) and truco!=4:
                if aggresive and randint(1,10) < 8 and truco!=4:
                    return True
                return False
        return None
