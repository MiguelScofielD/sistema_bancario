class Conta:
    def __init__(self, saldo):
        self.saldo = saldo
        self.n_saque = 0
        self.extrato_conta = ""

    def extrato(self):
        print("\n===============EXTRATO================")
        print(
            f"Não foram realizadas operações."
            if not self.extrato_conta
            else self.extrato_conta
        )
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("========================================")

    def depositar(self):
        deposito = float(input(f"Digite o valor do seu depósito: "))
        if deposito > 0:
            self.saldo += deposito
            print(f"Depósito de R${deposito} realizado com sucesso!")
            self.extrato_conta += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Operação falhou! o valor informado é inválido.")

    def saque(self):
        if self.n_saque <= 2:
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor > self.saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            else:

                if valor > 500:
                    print("Operação falhou! O valor do saque excede o limite.")
                else:
                    print(f"Saque de R${valor:.2f} efetuado com sucesso!")
                    self.saldo -= valor
                    self.n_saque += 1
                    self.extrato_conta += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Número máximo de saques excedido.")

    def sair(self):
        exit()

    def operacao(self):
        operacao = input(
            """ 
            [s] Saque
            [d] Depósito
            [e] Extrato
            [q] Sair
            
            => """
        )
        if operacao == "s":
            return self.saque()
        elif operacao == "d":
            return self.depositar()
        elif operacao == "e":
            return self.extrato()
        elif operacao == "q":
            return self.sair()


conta = Conta(500)
print(f"Saldo: R${conta.saldo:.2f}")

while True:
    conta.operacao()
