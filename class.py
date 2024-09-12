#llegamos a las clases en python. Recordando que un objeto no es mas que la forma de 
#representar algo en codigo, usualmente algo de la vida real.abs

#Esto se denota debido a que cuando creamos un objetos, estos tienen una propiedad y un valor,
#usualmente definido con this (en js) o self en python
#con self y uno de los nombre de las propiedades del objetos, estamos diciendo que el valor
#que va a tener cuando le pasemos un dato como parametro, va a ser el mismo que le dimos
#mediante self. pero dejame practicarlo mas que hablarlo.abs

class Car:
    def __init__(self, brand, color, model, price):
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price

    def getDetails(self):
        print(f'Bienvenido a BobaCar!, el carro que estas mirando ahora mismo, es un {self.brand} de color {self.color}, en el modelo {self.model} de {self.brand}. A tan solo {self.price} dolares! ')


tesla = Car('Tesla', 'Morado', 'S', 78000)
kia = Car('Kia', 'Rojo', 'Carens', 32000)

tesla.getDetails()
kia.getDetails()

#cuando usamos self, debemos pasarlo como forma de 'this'

#crear una cuenta bancaria

class BankAccount:
    def __init__(self, balance, account_name, bankName):
        self.balance = balance
        self.account_name = account_name
        self.bankName = bankName
        self.isActive = True

    def agregarSaldo(self, amount):
        if self.isActive:
            self.balance += amount
            print(f'Le has anadido un monto de {amount} a tu cuenta de {self.bankName}. Tu nuevo balance es de {self.balance} a nombre de {self.account_name} ')
        else:
            print('Tu cuenta esta inactiva.')

    def retirarSaldo(self, amount):
     if self.isActive: 
        if amount <= self.balance:
            self.balance -= amount
            print(f'Le has retirado {amount}$ a tu cuenta de {self.bankName}. Tu nuevo saldo es de {self.balance}')
        else:
            print(f'No tienes el saldo suficiente para retirar {amount} de tu cuenta. Tu saldo actual es de {self.balance} en tu cuenta del {self.bankName}')
    def deactivateAccount(self):
        self.isActive = False

    def activateAccount(self):
        self.isActive = True
    
Calvin = BankAccount(3000, 'Calvin Bobadilla', 'Popular')

Calvin.agregarSaldo(3000) 

Calvin.retirarSaldo(2000)
Calvin.retirarSaldo(6000)

Javier = BankAccount(2000, 'Javier Bobadilla', 'Qik')
Javier.activateAccount()
Javier.agregarSaldo(999999999999)

