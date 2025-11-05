class Game:
    total_jogos = 0 #Variavel da classe para contar o numero de jogos
    def __init__(self, nome="", anoLancamento=0, multiplayer=False, nota=0):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota
        Game.total_jogos += 1
        self.avaliacaoTotal = 0
        self.avaliadores = 0
    
    def __str__(self):
        return f"Game: {self.nome}"
    
    def ficha_tecnica(self):
        print("======Dados do jogo======")
        print(f"Nome do jogo: {self.nome}")
        print(f"Ano de lancamento: {self.anoLancamento}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Nota: {self.nota}\n")
        
    def avaliacao(self, nota):
        self.avaliacaoTotal += nota
        self.avaliadores += 1
        
    def media(self):
        print(f"Media do jogo {self.nome}: {self.avaliacaoTotal / self.avaliadores} ")
    
#  Subclasse

class SinglePlayer(Game):
        def __init__(self, nome="", anoLancamento=0, nota=0, historia=""):
            super().__init__(nome, anoLancamento, multiplayer=False, nota=nota)
            self.historia = historia
        
        def ficha_tecnica(self):
            super().ficha_tecnica()
            print(f"Enredo: {self.historia}")
            
mult_jogo = Game("Fortnite", 2017, True, 8.0)
mult_jogo.ficha_tecnica()

sing_jogo = SinglePlayer("The Last of Us 2", 2020, 9.5, "Emocionante historia de sobrevivencia")
sing_jogo.ficha_tecnica()