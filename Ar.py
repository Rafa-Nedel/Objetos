
class Arcondicionado:
    def __init__(self):
        self.ligado = False
        self.temp = 25

    def power(self):
        if self.ligado:
            self.ligado = False
        else:
            self.ligado = True

    def aumentar_temperatura(self):
        if self.ligado:
            self.temp += 1

    def diminuir_temperatura(self):
        if self.ligado:
            self.temp -= 1


controle_ar = Arcondicionado()
print(controle_ar.ligado)
controle_ar.power()
print(controle_ar.ligado, controle_ar.temp)
controle_ar.aumentar_temperatura()
print(controle_ar.temp)
controle_ar.diminuir_temperatura()
print(controle_ar.temp)
