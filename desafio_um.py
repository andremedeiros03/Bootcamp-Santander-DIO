LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500.00
deposito = 0
saldo = 0
saques = 0
saque = 0
extrato = ""
    
menu = """
[d] depositar
[s] sacar
[e] extrato
[q] sair

->"""

while True:

    opcao = input(menu)

    if opcao == 'd':
        print("Depósito")
        deposito = float(input("Realize seu depósito: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"++Depósito - R${deposito:.2f}\nSaldo atual: R${saldo}\n"
        else:
            print("Operação falhou! O valor informado é inválido")
        
    elif opcao == 's':
        print("Saque")
        saque = float(input("Informe o valor desejado para sacar: "))

        excedeu_limite = saques >= LIMITE_SAQUES
        saldo_zerado = saldo == 0
        excedeu_saldo = saque > saldo
        execedeu_valor_limite = saque > LIMITE_SAQUE_VALOR

        if excedeu_limite:
            print("Não é possível realizar a operação sacar mais do que 3 vezes")
        elif saldo_zerado:
            print("Não é possível realizar a operação, pois o seu saldo está zerado")
        elif excedeu_saldo:
            print(f"Operação não realizada porque o valor do saque R${saque:.2f} é maior do que o saldo da sua conta")
        elif execedeu_valor_limite:
            print("Não é possível sacar uma valor maior do que R$500")
        else:
            saldo -= saque
            extrato += f"--Saque - R${saque}\nSaldo atual: R${saldo}\n"
            #print(f"O valor R${saque:.2f} foi sacado com sucesso!")
            saques += 1
    elif opcao == 'e':
        print("Extrato")
        print("===========EXTRATO============")
        print("Não foram realizadas operações."if not extrato else extrato)
        print("==============================")

    elif opcao == 'q':
        print("Saindo...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")









