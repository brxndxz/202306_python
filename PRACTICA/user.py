class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.balance = 0
    def depositar(self, balance):
        self.balance += balance
        return self
    def retirar(self, balance):
        self.balance -= balance
        return self
    def mostrar_balance(self):
        print(f"Usuario: {self.nombre} Balance de Cuenta: {self.balance}")
        return self
    def transferir(self, balance, Usuario):
        self.balance -= balance
        Usuario.balance += balance
        self.mostrar_balance()
        Usuario.mostrar_balance()
        return self

guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
brenda = Usuario("Brenda", "brenda@python.com")

guido.depositar(50).depositar(25).depositar(30).retirar(20).mostrar_balance()

monty.depositar(60).depositar(30).retirar(15).retirar(20).mostrar_balance()

brenda.depositar(100).retirar(20).retirar(25).retirar(10).mostrar_balance()
print("-"*50)
guido.transferir(15, brenda)