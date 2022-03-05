
class Calc:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def dimi(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def divi(self):
        return self.a / self.b


prim = int(input('digite um número: '))
seg = int(input('digite outro número: '))
operacao = input('você quer somar, diminuir, dividir ou multiplicar? ')

calculadora = Calc(prim, seg)

if operacao == 'somar':
    resultado = ' O resultado da sua soma foi: {} '.format(
        calculadora.soma())
    print('\033[1;90m{}\033[m'.format(resultado))
elif operacao == 'diminuir':
    resultado = ' O resultado da sua diminuição foi: {} '.format(
        calculadora.dimi())
    print('\033[1;96m{}\033[m'.format(resultado))
elif operacao == 'dividir':
    resultado = ' O resultado da sua divisão foi: {} '.format(
        calculadora.divi())
    print('\033[1;93m{}\033[m'.format(resultado))
elif operacao == 'multiplicar':
    resultado = ' O resultado da sua multiplicação foi: {} '.format(
        calculadora.multi())
    print('\033[1;31m{}\033[m'.format(resultado))
