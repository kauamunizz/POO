class Game:
    def __init__(self, nome="", anoLancamento=0, multiplayer=False, nota=0):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota
    
    def __str__(self):
        return f"Game: {self.nome}"
    
jogo1 = Game("The Legend of Zelda", 2017, False, 4.5)
jogo2 = Game("Fortnite", 2017, True, 4)
# print(jogo1)

print("======Dados do jogo======")
print(f"Nome do jogo: {jogo1.nome}\nAno de lancamento: {jogo1.anoLancamento}\nMultiplayer: {jogo1.multiplayer}\nNota de 0 a 5: {jogo1.nota}")
print("======Dados do jogo======")
print(f"Nome do jogo: {jogo2.nome}\nAno de lancamento: {jogo2.anoLancamento}\nMultiplayer: {jogo2.multiplayer}\nNota de 0 a 5: {jogo2.nota}")