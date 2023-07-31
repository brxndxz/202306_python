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
        return self.balance
    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)
        return self


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0)
    def mostrar_balance(self):
        print(f"Usuario: {self.nombre} Balance de Cuenta: {self.cuenta.mostrar_info_cuenta()}")
        return self
    def transferir(self, monto, Usuario):
        self.monto -= monto
        Usuario.monto += monto
        self.mostrar_balance()
        Usuario.mostrar_balance()
        return self

brenda = Usuario("Brenda", "brenda@dojo.com")
brenda.cuenta.deposito(100).deposito(200)
brenda.mostrar_balance()