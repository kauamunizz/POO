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
    
    
jogo1 = Game("The Legend of Zelda", 2017, False, 9.5)
jogo2 = Game("Fortnite", 2017, True, 8.0)

jogo1.ficha_tecnica()
jogo2.ficha_tecnica()
jogo1.avaliacao(9.0)
jogo1.avaliacao(7.5)
jogo1.media()
jogo2.avaliacao(6.5)
jogo2.avaliacao(7.5)
jogo2.media()

# Quantidade de jogos
print(f"Quantidade de jogos criados: {Game.total_jogos}")