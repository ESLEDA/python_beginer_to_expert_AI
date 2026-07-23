class Perro:
    tamaño = 'mediano'
    def __init__(self, name = 'scuby', color = 'blanco'):
        self.name = name
        self.color = color
        
        
        


class Gato:
    pass

perro1 = Perro(name ='Pluto', color = 'cafe')
print(perro1.name, perro1.color)
print(perro1.tamaño)