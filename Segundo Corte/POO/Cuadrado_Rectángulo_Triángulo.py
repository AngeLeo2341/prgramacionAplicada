class Cuadrado:
    def area (self, lado):
        return lado ** 2
cuadrado = Cuadrado()
area = cuadrado.area(12)
print ('El área del cuadrado es {}'.format(area))
teaching_table_area = cuadrado.area(36)
print (teaching_table_area)

##############################################

class Rectangulo:
    def area (self, base, altura):
        return base * altura
rectangulo = Rectangulo()
area = rectangulo.area(4, 7)
print ('El área del rectangulo es {}'.format(area))
teaching_table_area = rectangulo.area(8, 9)
print (teaching_table_area)

##############################################

class Triangulo:
    def area (self, base, altura):
        return (base * altura)/ 2
triangulo = Triangulo()
area = triangulo.area(4, 7)
print ('El área del triángulo es {}'.format(area))
teaching_table_area = rectangulo.area(8, 9)
print (teaching_table_area)
