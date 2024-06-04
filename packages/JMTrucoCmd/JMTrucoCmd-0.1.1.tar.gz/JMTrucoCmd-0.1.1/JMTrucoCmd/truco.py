class Truco():
    def __init__(self,carta:str = '1 Espada') -> None:
        self.carta = carta
    
    def print_carta(self):
        print(f'Tu carta es: {self.carta}')
    
    def update_carta(self,carta:str = '1 Espada'):
        self.carta = carta
        print('Carta actualizada con exito')