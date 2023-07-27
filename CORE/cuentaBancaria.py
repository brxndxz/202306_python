class CuentaBancaria:
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
    def deposito(self, monto):
        self.balance += monto
        return self
    def retiro(self,monto):
        if self.balance >= monto:
            self.balance -= monto
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self
    def mostrar_info_cuenta(self):
        print("Balance:", self.balance)
        return self
    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)
        return self

cuenta1 = CuentaBancaria(0.02, 200)
cuenta2 = CuentaBancaria(0.04, 200)

cuenta1.deposito(30).deposito(50).deposito(20).retiro(50).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(50).deposito(50).retiro(100).retiro(100).retiro(100).generar_interes().mostrar_info_cuenta()

#depósito(self, amount): aumenta el balance de la cuenta en el monto dado
#retiro(self, amount): disminuye el balance de la cuenta en el monto dado si hay fondos suficientes; 
#si no hay suficiente dinero, imprime el mensaje: "Fondos insuficientes: cobrando una tarifa de $5", y resta $5
#mostrar_info_cuenta(self)imprime en la consola: por ejemplo, "Balance: $100"
#generar_interés(self): aumenta el balance de la cuenta por el balance actual * la tasa de interés
#(siempre que el balance sea positivo)