from publicacion import Publicacion
class Revista(Publicacion):
    def __init__(self, titulo, año_publicacion, numero_revista, nombre_revista):
        super().__init__(titulo, año_publicacion)
        self.numero_revista = numero_revista
        self.nombre_revista = nombre_revista
    
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Número de la revista: {self.numero_revista}, Nombre de la revista: {self.nombre_revista}")

if __name__ == "__main__":
    revista = Revista("Editorial Sudamericana", 1967, 50, "Sudamericana")
    revista.mostrarInfo()
