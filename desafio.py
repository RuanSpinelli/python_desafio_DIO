menu = """

[d] DEPOSITAR
[s] SACAR 
[e] EXTRATO
[q] SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou por valor inválido!")


    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excerdeu_saldo = valor > saldo
        excerdeu_limite = valor > limite
        excerdeu_saques = numero_saques > LIMITE_SAQUES
    
        if excerdeu_saldo:
            print("Operação falhou! Não há saldo suficiente.")
        elif excerdeu_limite:
            print("Operação falhou! O valor é maior que o limite.")
        elif excerdeu_saques:
            print("Operação falhou! não há mais saques disponíveis por hoje.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1    
            print("Saque realizado com sucesso!")


    elif opcao == "e":
        
        print("\n", "=" *8, " EXTRATO ", "=" *8 )
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo = R${saldo:.2f}")
        print("=" * 25)


    elif opcao == "q":
        break


    else:
        print("Opção inválida! por favor tente novamente!")