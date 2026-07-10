import random
# Pedra, papel, tesoura print(f"Você escolheu {player} e o computador escolheu {computador}, você perdeu! :()")
print("Pedra, papel e tesoura (🪨📄✂️)! ")

while True:

 player = input(("Escolha Pedra, papel ou tesoura, ou digite sair para sair! : ")).lower()



 computador = random.choice(["pedra", "papel", "tesoura"])

 if player == "pedra" and computador == "papel":
    print(f"Você escolheu {player} e o computador escolheu {computador}, você perdeu! :()")
 elif player == "pedra" and computador == "tesoura":
    print(f"Você escolheu {player} e o computador escolheu {computador}, você venceu! :))")
 elif player == computador:
    print(f"Empate! Ambos escolheram {player}")
 elif player == "papel" and computador == "pedra":
    print(f"Você venceu: Você escolheu {player} e o computador escolheu {computador}")
 elif player == "papel" and computador == "tesoura":
    print(f"Você perdeu! Você escolheu {player} e o computador escolheu {computador}")
 elif player == "tesoura" and computador == "papel":
    print(f"Você venceu! Você escolheu {player} e o computador escolheu {computador}")
 elif player == "tesoura" and computador == "pedra":
    print(f"Você perdeu: Você escolheu {player} e o computador escolheu {computador}")
 elif player == "sair":
    print("você saiu!")
    break