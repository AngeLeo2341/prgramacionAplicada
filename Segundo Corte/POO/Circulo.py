class Circulo:
    pi = 3.1415
    def __init__(self, diameter):
        print ('Nuevo circulo con diametro: {}'.format(diameter))
teaching_table = Circulo(36)

##################################################################

class Circulo:
    pi = 3.1415
    def area (self, radius):
        return Circulo.pi * radius ** 2
circulo = Circulo()
pizza_area = circulo.area(12/2)
print (pizza_area)
teaching_table_area = circulo.area(36/2)
print (teaching_table_area)

##################################################################

class Circulo:
    pi = 3.1415
    def __init__(self, diametro):
        print("Creando circulo con diametro {d}".format(d=diametro))
        self.radius = diametro/2
    def circunferencia(self):
        return 2*self.pi*self.radius
pizza_mediana = Circulo(12)
teaching_table = Circulo(36)
round_room = Circulo(11460)
print(pizza_mediana.circunferencia())
print(teaching_table.circunferencia())
print(round_room.circunferencia())
