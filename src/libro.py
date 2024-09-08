class Libro:
    def __init__(self, titulo, año_publicacion, autor, num_paginas):
        self.titulo = titulo
        self.año_publicacion = año_publicacion
        self.autor = autor
        self.num_paginas = num_paginas
    
    def mostrarInfo(self):
        print(f"Título: {self.titulo}, Año de publicación: {self.año_publicacion}")
        print(f"Autor: {self.autor}, Número de páginas: {self.num_paginas}")

if __name__ == "__main__":
    libro = Libro("Cien años de soledad", 1967, "Gabriel Garcia Márquez", 447)
    libro.mostrarInfo()
