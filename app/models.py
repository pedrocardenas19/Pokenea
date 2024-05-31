class Pokenea:
    def __init__(self, id, nombre, altura, habilidad, imagen, frase):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.habilidad = habilidad
        self.imagen = imagen
        self.frase = frase

POKENEAS = [
    Pokenea(1, 'Pokenea1', 1.2, 'Habilidad1', 'https://storage.googleapis.com/bucket/pokenea1.jpg', 'Frase filosófica 1'),
    Pokenea(2, 'Pokenea2', 1.5, 'Habilidad2', 'https://storage.googleapis.com/bucket/pokenea2.jpg', 'Frase filosófica 2'),
    Pokenea(3, 'Pokenea3', 1.3, 'Habilidad3', 'https://storage.googleapis.com/bucket/pokenea3.jpg', 'Frase filosófica 3'),
    Pokenea(4, 'Pokenea4', 1.4, 'Habilidad4', 'https://storage.googleapis.com/bucket/pokenea4.jpg', 'Frase filosófica 4'),
    Pokenea(5, 'Pokenea5', 1.1, 'Habilidad5', 'https://storage.googleapis.com/bucket/pokenea5.jpg', 'Frase filosófica 5'),
    Pokenea(6, 'Pokenea6', 1.6, 'Habilidad6', 'https://storage.googleapis.com/bucket/pokenea6.jpg', 'Frase filosófica 6'),
    Pokenea(7, 'Pokenea7', 1.7, 'Habilidad7', 'https://storage.googleapis.com/bucket/pokenea7.jpg', 'Frase filosófica 7'),
]
