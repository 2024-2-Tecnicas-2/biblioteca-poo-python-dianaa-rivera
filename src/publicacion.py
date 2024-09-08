class Publicacion:
    def __init__(self, titulo, año_publicacion):

        self.titulo = titulo
        self.año_publicacion = año_publicacion
    
    def mostrarInfo(self):

        print(f"Título: {self.titulo}, Año de publicación: {self.año_publicacion}")
