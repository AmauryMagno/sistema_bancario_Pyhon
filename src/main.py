from decimal import Decimal

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    # Todos os depositos devem ser armazenados em saldo
    if opcao == "d":
        print("Deposito")
        valor = float(input("Qual valor deseja depositar: "))
        saldo += Decimal(valor)
        extrato += f"DEPOSITO: R$ {valor:.2f} \n"

    elif opcao == "s":
        print("Saque")
        if numero_saques <= LIMITE_SAQUES:
            valor = float(input("Qual valor deseja sacar: "))
            if valor > limite:
                print("O saque deve ser menor que R$ 500.00")
            elif valor > saldo:
                print("Saldo insuficiente")
            else:
                saldo -= Decimal(valor)
                numero_saques += 1
                extrato += f"SAQUE: R$ {valor:.2f} \n"
        else:
            print("Limite de 3 saques diarios excedido")
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operacao invalida, pro favor selecione novamente a operacao desejada.")
