
'''2. Crie a função chamada cria_conta( ), que recebe como argumento numero, titular, saldo e
limite.

3. Dentro de cria_conta(), crie uma variável do tipo dicionário chamada conta com as chaves
recebendo os valores dos parâmetros (numero, titular, saldo, tipo de conta e limite ), e ao
final, retorne a conta.'''

#Functions for creating and updating
class ContaBancaria:
        
    def cria_conta(numero, titular, saldo, limite):
        #dictionary of variables
        tipo_conta = int(input(f"Digite o tipo da conta: \n[1]Corrente [2]Poupança:\n"))

        if tipo_conta == 1:
            tipo_conta = "Corrente"
        if tipo_conta == 2:
            tipo_conta = "Poupança"

        conta = {"numero": numero,
                "titular": titular,
                "saldo": saldo,
                "tipo_conta": tipo_conta,
                "limite": limite}
        return conta



    '''4. Crie uma função chamada deposita( ) no mesmo arquivo que recebe com argumento uma
    conta e um valor. Dentro da função, adicione o valor ao saldo nos tipo de conta.'''

    #Function that receive value to balance
    def deposita(conta, valor):
        conta['saldo'] += valor

    '''5. Crie outra função chamada saca( ) ao qual usuário possa escolher em qual tipo de conta ele
    deseja sacar o valor, que recebe como argumento um conta, tipo de conta e um valor. Dentro
    da função, subtraia o valor do saldo.
    '''
    #function to check account type and make a withdrawal #função para verificar tipo de conta e realizar um saque 
    def saca(conta, tipo_conta, valor):
        tipo_conta = tipo_conta
        if valor <= conta['saldo']:
            conta['saldo'] -= valor
            print(f'Saque {valor} realizado com sucesso. Saldo atual: {conta["saldo"]}')

        else:
            print(f'Saldo insuficiente na conta')


    '''6. E por fim, crie uma função chamada extrato( ), que recebe como argumento uma conta e
    imprima o numero e o saldo.'''

    def extrato (conta):
        print(f'O número da conta é: {conta["numero"]}')
        print(f'Com saldo atual de {conta["saldo"]}')


                
