class Game:
    nome = ""
    anoLancamento = 0
    multiplayer = False
    nota = 0
    
# Primeiro jogo
jogo1 = Game()
jogo1.nome = "Apex Legends"
jogo1.anoLancamento = 2019
jogo1.multiplayer = True
jogo1.nota = 3.5

print("======Dados do jogo======")
print(f"Nome do jogo: {jogo1.nome}\nAno de lancamento: {jogo1.anoLancamento}\nMultiplayer: {jogo1.multiplayer}\nNota de 0 a 5: {jogo1.nota}")

# Segundo jogo
jogo2 = Game()
jogo2.nome = "Fortnite"
jogo2.anoLancamento = 2017
jogo2.multiplayer = True
jogo2.nota = 4

print("======Dados do jogo======")
print(f"Nome do jogo: {jogo2.nome}\nAno de lancamento: {jogo2.anoLancamento}\nMultiplayer: {jogo2.multiplayer}\nNota de 0 a 5: {jogo2.nota}")