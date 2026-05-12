operador = 0
op = False

class Pilha:

    def __init__(self):
        self.itens = []
        self.size = 0

    def add(self, number):
        if self.size < 4:
            self.itens.append(number)
            self.size += 1
        else:
            for i in range(4):
                if i < 3:
                    self.itens[i] = self.itens[i + 1]
                else:
                    self.itens[3] = number
        self.list()

    def operate(self, option):
        if len(self.itens) > 1:
            if option == "+":
                self.itens[-2] = self.itens[-2] + self.itens[-1]
            elif option == "-":
                self.itens[-2] = self.itens[-2] - self.itens[-1]
            elif option == "/":
                self.itens[-2] = self.itens[-2] / self.itens[-1]
            elif option == "*":
                self.itens[-2] = self.itens[-2] * self.itens[-1]
            else:
                print("Operador invC!lido.")
                return
            self.itens.pop()
            print(f"Resultado {self.itens[-1]}")
            return True

    def list(self):
        j = 0
        if len(self.itens) == 0:
            print("Lista vazia")
            return

        print("\n")
        try:
            print(f"X {self.itens[0]}")
        except IndexError:
            print(f"X 0")
        try:
            print(f"Y {self.itens[1]}")
        except IndexError:
            print(f"Y 0")
        try:
            print(f"Z {self.itens[2]}")
        except IndexError:
            print(f"Z 0")
        try:
            print(f"T {self.itens[3]}")
        except IndexError:
            print(f"T 0")


def is_number(s):
    try:
        float(s)
        return True
    except error:
        return False


pilha = Pilha()
while True:

    option = input("Input: \n")
    if option == "listar":
        pilha.list()
    elif option == "cls":
        pilha.itens.clear()
        operador = 0
        print("Limpo")
    elif option == "break":
        break
    else:
        operation = option.split()
        numbers = []
        operators = []
        for n in operation:
            try:
                pilha.add(float(n))
                numbers.append(n)
            except ValueError:
                op = pilha.operate(n)
                pilha.list()
                operators.append(n)

        if numbers != []:
            n1 = numbers.pop(0)
            n2 = numbers.pop(0)

        if operators != []:
            if numbers == []:
                numbers = pilha.itens.copy()
            result = f"( {n1} {operators[0]} {n2} )"
            operators.pop(0)
            for o in operators:
                n1 = numbers.pop(0)
                result += f"( {result} {o} {n1} )"



        if op == True:
            print(f"A expressão algébrica é: {result}")
