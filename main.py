#Projeto aula (comentário teste)

from contaBancaria import ContaBancaria as Conta


minha_conta = Conta.cria_conta('12345', 'João', 1000, 500)

print('número da conta:', minha_conta["numero"])
print('titular da conta:', minha_conta["titular"])
print('Saldo Inicial: ', minha_conta["saldo"])
print('tipo da conta:', minha_conta["tipo_conta"])

deposito = int(input('Digite o valor do depósito: '))
Conta.deposita(minha_conta, deposito)
print(f"Depósito de {deposito} realizado. Saldo atual: {minha_conta['saldo']}")

saque = float(input("Digite o valor a ser sacado: "))
Conta.saca(minha_conta, minha_conta, saque)

print("Extrato da conta:")
Conta.extrato(minha_conta)