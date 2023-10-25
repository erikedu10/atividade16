situacao = input("Você é idoso, gestante, cadeirante ou nenhum destes? Digite 'idoso', 'gestante', 'cadeirante' ou 'nenhum': ")

if situacao == "idoso" or situacao == "gestante" or situacao == "cadeirante":
    print("Você tem acesso à fila de prioridade.")
else:
    print("Você não tem acesso à fila de prioridade.")