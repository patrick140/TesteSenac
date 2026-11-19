anniversariante = input("Anniversariante? (sim/nao)")
ingresso = input("Tem ingresso? (sim/nao)")

if anniversariante == "sim":
    anniversariante = True
else:
    anniversariante = False

if ingresso == "sim":
    ingresso = True
else:
    ingresso = False


if anniversariante == True or ingresso == True:
    print("Acesso liberado")
else:
    print("Acesso negado, Compre um ingresso")

